import codecs
import logging
import os
from copy import deepcopy

logging.getLogger().setLevel(logging.INFO)
from collections import OrderedDict

import numpy as np
import rmgpy.molecule.element as elements
from joblib import Parallel, delayed
from rmgpy.data.base import (Database, DatabaseError, Entry, LogicOr,
                             remove_comment_from_line, make_logic_node)
from rmgpy.data.thermo import ThermoData, add_thermo_data, save_entry
from rmgpy.molecule.atomtype import ATOMTYPES
from rmgpy.molecule.group import Group
from rmgpy.reaction import same_species_lists
from sklearn.model_selection import KFold


def average_thermo_data(thermo_data_list=None, weighted=False, bounded=False):
    """
    Average a list of ThermoData values together.
    Sets uncertainty values to be the approximately the 95% confidence interval, equivalent to
    2 standard deviations calculated using the sample standard variance:
    
    Uncertainty = 2s
    s = sqrt( sum(abs(x - x.mean())^2) / N - 1) where N is the number of values averaged
    
    Note that uncertainties are only computed when number of values is greater than 1.
    """
    if thermo_data_list is None:
        thermo_data_list = []

    num_values = len(thermo_data_list)

    if num_values == 0:
        raise ValueError('No thermo data values were inputted to be averaged.')
    else:
        logging.debug('Averaging thermo data over {0} value(s).'.format(num_values))

        if not weighted:
            if num_values == 1:
                return deepcopy(thermo_data_list[0])

            else:
                averaged_thermo_data = deepcopy(thermo_data_list[0])
                for thermo_data in thermo_data_list[1:]:
                    averaged_thermo_data = add_thermo_data(averaged_thermo_data, thermo_data)

                for i in range(averaged_thermo_data.Tdata.value_si.shape[0]):
                    averaged_thermo_data.Cpdata.value_si[i] /= num_values

                    cp_data = [thermo_data.Cpdata.value_si[i] for thermo_data in thermo_data_list]
                    averaged_thermo_data.Cpdata.uncertainty_si[i] = 2 * np.std(cp_data, ddof=1)

                h_data = [thermo_data.H298.value_si for thermo_data in thermo_data_list]
                averaged_thermo_data.H298.value_si /= num_values
                averaged_thermo_data.H298.uncertainty_si = 2 * np.std(h_data, ddof=1)

                s_data = [thermo_data.S298.value_si for thermo_data in thermo_data_list]
                averaged_thermo_data.S298.value_si /= num_values
                averaged_thermo_data.S298.uncertainty_si = 2 * np.std(s_data, ddof=1)
                return averaged_thermo_data
            
        else:
            averaged_thermo_data = deepcopy(thermo_data_list[0])
            
            if num_values == 1:
                averaged_thermo_data.H298.uncertainty
                return averaged_thermo_data

            else:
            
                h_data = [thermo_data.H298.value_si for thermo_data in thermo_data_list]
                h_weights = [1/(thermo_data.H298.uncertainty_si)**2 for thermo_data in thermo_data_list]
                h_avg = np.average(h_data, weights=h_weights)
                h_std = np.sqrt(np.cov(h_data, aweights=h_weights, ddof=1))
                averaged_thermo_data.H298.value_si = h_avg
                averaged_thermo_data.H298.uncertainty_si = 2 * h_std
                if bounded:
                    max_h_unc = max(thermo_data.H298.uncertainty_si for thermo_data in thermo_data_list)
                    averaged_thermo_data.H298.uncertainty_si = np.sqrt(averaged_thermo_data.H298.uncertainty_si**2 + max_h_unc**2)

                s_data = [thermo_data.S298.value_si for thermo_data in thermo_data_list]
                s_weights = [1/(thermo_data.S298.uncertainty_si)**2 for thermo_data in thermo_data_list]
                s_avg = np.average(s_data, weights=s_weights)
                s_std = np.sqrt(np.cov(s_data, aweights=s_weights, ddof=1))
                averaged_thermo_data.S298.value_si = s_avg
                averaged_thermo_data.S298.uncertainty_si = 2 * s_std
                if bounded:
                    max_s_unc = max(thermo_data.S298.uncertainty_si for thermo_data in thermo_data_list)
                    averaged_thermo_data.S298.uncertainty_si = np.sqrt(averaged_thermo_data.S298.uncertainty_si**2 + max_s_unc**2)

                for i in range(averaged_thermo_data.Tdata.value_si.shape[0]):
                    cp_data = [thermo_data.Cpdata.value_si[i] for thermo_data in thermo_data_list]
                    cp_weights = [1/(thermo_data.Cpdata.uncertainty_si[i])**2 for thermo_data in thermo_data_list]
                    cp_avg = np.average(cp_data, weights=cp_weights)
                    cp_std = np.sqrt(np.cov(cp_data, aweights=cp_weights, ddof=1))
                    averaged_thermo_data.Cpdata.value_si[i] = cp_avg
                    averaged_thermo_data.Cpdata.uncertainty_si[i] = 2 * cp_std
                    if bounded:
                        max_cp_unc = max(thermo_data.Cpdata.uncertainty_si[i] for thermo_data in thermo_data_list)
                        averaged_thermo_data.Cpdata.uncertainty_si[i] = np.sqrt(averaged_thermo_data.Cpdata.uncertainty_si[i]**2 + max_cp_unc**2)

                return averaged_thermo_data

class ThermoGroups(Database):
    """
    A class for working with an RMG thermodynamics group additivity database.
    """

    def __init__(self, label='', name='', short_desc='', long_desc='', metal=None, site=None, facet=None):
        Database.__init__(self, label=label, name=name, short_desc=short_desc, long_desc=long_desc,
                          metal=metal, site=site, facet=facet)

    def load_entry(self,
                   index,
                   label,
                   group,
                   thermo,
                   reference=None,
                   referenceType='',
                   shortDesc='',
                   longDesc='',
                   rank=None,
                   metal=None,
                   facet=None,
                   site=None,
                   ):
        """
        Method for parsing entries in database files.
        Note that these argument names are retained for backward compatibility.
        """

        if (group[0:3].upper() == 'OR{' or
                group[0:4].upper() == 'AND{' or
                group[0:7].upper() == 'NOT OR{' or
                group[0:8].upper() == 'NOT AND{'):
            item = make_logic_node(group)
        else:
            item = Group().from_adjacency_list(group)
        self.entries[label] = Entry(
            index=index,
            label=label,
            item=item,
            data=thermo,
            reference=reference,
            reference_type=referenceType,
            short_desc=shortDesc,
            long_desc=longDesc.strip(),
            rank=rank,
            metal=metal,
            facet=facet,
            site=site,
        )

    def save_entry(self, f, entry):
        """
        Write the given `entry` in the thermo database to the file object `f`.
        """
        return save_entry(f, entry)

    def generate_old_library_entry(self, data):
        """
        Return a list of values used to save entries to the old-style RMG
        thermo database based on the thermodynamics object `data`.
        """

        return generate_old_library_entry(data)

    def process_old_library_entry(self, data):
        """
        Process a list of parameters `data` as read from an old-style RMG
        thermo database, returning the corresponding thermodynamics object.
        """
        return process_old_library_entry(data)

    def copy_data(self, source, destination):
        """
        This method copys the ThermoData object and all meta data
        from source to destination
        Args:
            source: The entry for which data is being copied
            destination: The entry for which data is being overwritten

        """
        destination.data = source.data
        destination.reference = source.reference
        destination.short_desc = source.short_desc
        destination.long_desc = source.long_desc
        destination.rank = source.rank
        destination.reference_type = source.reference_type
        destination.metal = source.metal
        destination.facet = source.facet
        destination.site = source.site

    def remove_group(self, group_to_remove):
        """
        Removes a group that is in a tree from the database. For thermo
        groups we also, need to re-point any unicode thermo_data that may
        have pointed to the entry.

        Returns the removed group
        """

        # First call base class method
        Database.remove_group(self, group_to_remove)

        parent_r = group_to_remove.parent

        # look for other pointers that point toward entry
        for entry in self.entries.values():
            if isinstance(entry.data, str):
                if entry.data == group_to_remove.label:
                    # if the entryToRemove.data is also a pointer, then copy
                    if isinstance(group_to_remove.data, str):
                        entry.data = group_to_remove.data
                    # if the parent points toward entry and the data is
                    # not a base string, we need to copy the data to the parent
                    elif entry is parent_r:
                        self.copy_data(group_to_remove, parent_r)
                    # otherwise, point toward entryToRemove's parent
                    else:
                        entry.data = str(parent_r.label)

        return group_to_remove
    
    def match_mol_to_entries(self, mols_corrections):
        mol, correction = mols_corrections
        root = self.top[0]
        matched_entry_labels = []
        try:
            flag = not self.is_entry_match(mol, root, resonance=True)
        except:
            flag = not self.is_entry_match(mol, root, resonance=False)

        if flag:
            logging.error(root.item.to_adjacency_list())
            logging.error(mol.to_adjacency_list())
            raise ValueError('molecule: {0} does not match top node of {1}'.format(mol, self.label))

        matched_entry_labels.append(root.label)

        entry = root

        while entry.children != []:
            for child in entry.children:
                if self.is_entry_match(mol, child, resonance=False):
                    entry = child
                    matched_entry_labels.append(child.label)
                    break
            else:
                break
        return (mols_corrections, matched_entry_labels)

    def get_molecule_matches(self, mols_corrections, exact_matches_only=False, n_jobs=1):
        """
        returns a dictionary mapping for each entry in the tree:  
        (entry.label,entry.item) : list of all molecules (or the list given) that match that entry
        """
        logging.info("Getting molecule matches...")

        entries = self.entries

        assert len(set(entries.keys())) == len(entries.keys()), 'there are duplicate indices in family.group.entries'

        mol_lists = {entry.label: [] for entry in entries.values()}
        
        mols_corrections_matched_entry_labels = Parallel(n_jobs=n_jobs, verbose=5, backend='multiprocessing')(delayed(self.match_mol_to_entries)(mol_correction) for mol_correction in mols_corrections)
        for mol, matched_entry_labels in mols_corrections_matched_entry_labels:
            for entry_label in matched_entry_labels:
                mol_lists[entry_label].append(mol)

        if exact_matches_only:
            new_lists = dict()
            for key, ms in mol_lists.items():
                newms = set(ms)
                for child in self.entries[key].children:
                    newms -= set(mol_lists[child.label])
                new_lists[key] = list(newms)
            mol_lists = new_lists

        return mol_lists
    
    def is_entry_match(self, mol, entry, resonance=True):
        """
        determines if the labeled molecule object of reactants matches the entry
        """
        if isinstance(entry.item, Group):
            if resonance:
                structs = mol.generate_resonance_structures()
            else:
                structs = [mol]
            return any([mol.is_subgraph_isomorphic(entry.item, generate_initial_map=True) for mol in structs])
        elif isinstance(entry.item, LogicOr):
            return any([self.is_entry_match(mol, self.entries[c], resonance=resonance)
                        for c in entry.item.components])
        
    def mols_match_node(self, node, mols_corrections):
        for mol, correction in mols_corrections:
            if not self.is_entry_match(mol, node, resonance=False):
                return False

        return True
        
    def get_training_set(self, thermo_database):
        
        #TODO
        pass
    
    def make_tree_nodes(self, template_mol_map=None, obj=None, Ts=None, nprocs=0, depth=0, min_splitable_entry_num=2,
                        min_mols_corrections_to_spawn=20, extension_iteration_max=np.inf, extension_iteration_item_cap=np.inf, min_mols_corrections_to_split=1, n_jobs=1,
                        use_aleatoric_prepruning=False, aleatoric_prepruning_function=min,
                        use_model_variance_prepruning=False, model_variance_prepruning_threshold=0.05,):

        if depth > 0:
            root = self.entries[list(template_mol_map.keys())[0]]
        else:
            for entry in self.entries.values():  # find the root entry for this branch
                if entry.index != -1:
                    root = entry
                    break
            while root.parent is not None:
                root = root.parent

        if depth == 0: #may start with molecules at many nodes first iterationation
            psize = 0.0
            entries = [root]
            while entries != []:
                entry = entries[-1]
                if entry.children:
                    psize += float(len(template_mol_map[entry.label]))
                    entries.extend(entry.children)
                    entries.remove(entry)
                else:
                    psize += float(len(template_mol_map[entry.label]))
                    entries.remove(entry)
        else:
            psize = float(len(template_mol_map[root.label]))
            
        logging.info(f"Number of datapoints: {psize}")
        mult_completed_nodes = []  # nodes containing multiple identical training molecules
        prepruned_nodes = []
        boo = True  # if the for loop doesn't break becomes false and the while loop terminates
        active_procs = []
        active_conns = []
        active_proc_num = []
        proc_names = []
        free_procs = nprocs
        extra_entries = []
        r = None

        while boo:
            logging.info(f"Tree size: {len(template_mol_map)}")
            splitable_entry_num = 0
            for label, items in template_mol_map.items():  # figure out how many splitable objects there are
                entry = self.entries[label]
                if len(items) > min_mols_corrections_to_split and entry not in mult_completed_nodes:
                    splitable_entry_num += 1

            for label in list(template_mol_map.keys()):
                entry = self.entries[label]
                if not isinstance(entry.item, Group):  # skip logic nodes
                    continue
                if len(template_mol_map[label]) == 0:
                    continue
                if use_aleatoric_prepruning:
                    if entry in prepruned_nodes:
                        continue
                    if len(template_mol_map[label]) > 1:
                        corrections = [x[1] for x in template_mol_map[label]]
                        averaged_correction = average_thermo_data(corrections, weighted=True)
                        h_data_unc = aleatoric_prepruning_function(correction.H298.uncertainty_si for correction in corrections)
                        h_pred_unc = averaged_correction.H298.uncertainty_si
                        s_data_unc = aleatoric_prepruning_function(correction.S298.uncertainty_si for correction in corrections)
                        s_pred_unc = averaged_correction.S298.uncertainty_si
                        cp_data_uncs = np.array([aleatoric_prepruning_function(correction.Cpdata.uncertainty_si[i] for correction in corrections) for i in range(averaged_correction.Tdata.value_si.shape[0])])
                        cp_pred_uncs = averaged_correction.Cpdata.uncertainty_si
                        # logging.info(f"Data uncertainty: {h_data_unc}, {s_data_unc}, {cp_data_uncs}")
                        # logging.info(f"Pred uncertainty: {h_pred_unc}, {s_pred_unc}, {cp_pred_uncs}")
                        if h_data_unc > h_pred_unc and s_data_unc > s_pred_unc and all(cp_data_uncs > cp_pred_uncs):
                            logging.info(f"Prepruning {label} due to aleatoric uncertainty")
                            prepruned_nodes.append(entry)
                            continue

                if entry.index != -1 and len(template_mol_map[entry.label]) > min_mols_corrections_to_split and entry not in mult_completed_nodes and entry not in prepruned_nodes:
                    boo2, r = self.extend_node(entry, template_mol_map, obj=obj, Ts=Ts, r=r, iteration_max=extension_iteration_max, iteration_item_cap=extension_iteration_item_cap, use_model_variance_prepruning=use_model_variance_prepruning, model_variance_prepruning_threshold=model_variance_prepruning_threshold)
                    if boo2:  # extended node so restart while loop
                        break
                    else:  # no extensions could be generated since all molecules were identical
                        mult_completed_nodes.append(entry)
            else:
                if len(active_procs) == 0:
                    boo = False

            # fix indicies
            iterations = 0
            for entry in self.entries.values():
                if entry.index != -1:
                    entry.index = iterations
                    iterations += 1

        for label, entry in self.entries.items():
            if entry.index != -1 and entry.parent is None and entry.label != root.label:
                pname = "_".join(label.split('_')[:-1])
                while pname not in self.entries.keys():
                    pname = "_".join(label.split('_')[:-1])
                entry.parent = self.entries[pname]
                entry.parent.children.append(entry)

        return
    
    def extend_node(self, parent, template_mol_map, obj=None, Ts=None, r=None, iteration_max=np.inf, iteration_item_cap=np.inf, use_model_variance_prepruning=False, model_variance_prepruning_threshold=0.05):
        """
        Constructs an extension to the group parent based on evaluation 
        of the objective function obj
        """
        exts, gave_up_split = self.get_extension_edge(parent, template_mol_map, obj=obj, Ts=Ts, r=r, iteration_max=iteration_max, iteration_item_cap=iteration_item_cap)

        if exts == [] and not gave_up_split:  # should only occur when all molecules at this node are identical
            ms = template_mol_map[parent.label]
            for q, mol_correction in enumerate(ms):
                mol, correction, = mol_correction
                for j in range(q):
                    if not same_species_lists([mol], [ms[j][0]], generate_initial_map=True):
                        for p, atm in enumerate(parent.item.atoms):
                            if atm.reg_dim_atm[0] != atm.reg_dim_atm[1]:
                                logging.error('atom violation')
                                logging.error(atm.reg_dim_atm)
                                logging.error(parent.label)
                                logging.error('Regularization dimension suggest this node can be expanded, '
                                              'but extension generation has failed')
                            if atm.reg_dim_u[0] != atm.reg_dim_u[1]:
                                logging.error('radical violation')
                                logging.error(atm.reg_dim_u)
                                logging.error(parent.label)
                                logging.error('Regularization dimension suggest this node can be expanded, '
                                              'but extension generation has failed')
                        for p, bd in enumerate(parent.item.get_all_edges()):
                            if bd.reg_dim[0] != bd.reg_dim[1]:
                                logging.error('bond violation')
                                logging.error(bd.order)
                                logging.error(bd.reg_dim)
                                logging.error(parent.label)
                                logging.error('Regularization dimension suggest this node can be expanded, '
                                              'but extension generation has failed')

                        logging.error('split violation')
                        logging.error('parent')
                        logging.error(parent.item.to_adjacency_list())
                        for c, atm in enumerate(parent.item.atoms):
                            logging.error(c)
                            logging.error(atm.reg_dim_atm)
                            logging.error(atm.reg_dim_u)
                        logging.error("bonds:")
                        for bd in parent.item.get_all_edges():
                            ind1 = parent.item.atoms.index(bd.vertex1)
                            ind2 = parent.item.atoms.index(bd.vertex2)
                            logging.error(((ind1, ind2), bd.order, bd.reg_dim))
                        for mol_correction in ms:
                            mol = mol_correction[0]
                            logging.error(str(mol))
                            logging.error(mol.to_smiles())
                            logging.error(mol.to_adjacency_list())
                        logging.error("Clearing Regularization Dimensions and Reattempting")  # this usually happens when node expansion breaks some symmetry
                        parent.item.clear_reg_dims()  # this almost always solves the problem
                        R = elements.bde_elements
                        R = [ATOMTYPES[x].specific for x in R]
                        R = [specific for specifics in R for specific in specifics]
                        R.append(ATOMTYPES["H"])
                        return (True, R)
            return (False, None)
        
        if gave_up_split:
            return (False, None)
        
        vals = []
        for grp, grpc, name, typ, einds in exts:
            val, boo = self.eval_ext(parent, grp, name, template_mol_map, obj=obj, Ts=Ts)
            vals.append(val)

        min_val = min(vals)

        min_ind = vals.index(min_val)

        ext = exts[min_ind]

        if use_model_variance_prepruning:
            grp, grpc, name, typ, einds = ext

            mols_corrections = template_mol_map[parent.label]
            new, old, new_inds = self._split_molecules(mols_corrections, grp)
            if obj:
                parent_ob, boo = get_objective_function(mols_corrections, [], obj, Ts=Ts)
            else:
                parent_ob, boo = get_objective_function(mols_corrections, [], Ts=Ts)
            if (parent_ob - min_val) / parent_ob < model_variance_prepruning_threshold:
                logging.info(f"Parent objective function value: {parent_ob}")
                logging.info(f"New split objective function value: {min_val}")
                logging.info(f"Prepruning {name} due to small information gain quantified by model variance {(parent_ob - min_val) / parent_ob:.2e} < {model_variance_prepruning_threshold}")
                return (False, None)

        extname = ext[2]

        if ext[3] == 'atomExt':
            ext[0].atoms[ext[4][0]].reg_dim_atm = [ext[0].atoms[ext[4][0]].atomtype, ext[0].atoms[ext[4][0]].atomtype]
        elif ext[3] == 'elExt':
            ext[0].atoms[ext[4][0]].reg_dim_u = [ext[0].atoms[ext[4][0]].radical_electrons,
                                                 ext[0].atoms[ext[4][0]].radical_electrons]

        self.add_entry(parent, ext[0], extname)

        complement = not ext[1] is None

        if complement:
            frags = extname.split('_')
            frags[-1] = 'N-' + frags[-1]
            cextname = ''
            for k in frags:
                cextname += k
                cextname += '_'
            cextname = cextname[:-1]

            self.add_entry(parent, ext[1], cextname)

        mols_corrections = template_mol_map[parent.label]

        comp_entries = []
        new_entries = []

        for i, entry in enumerate(template_mol_map[parent.label]):
            if self.molecule_matches(entry, ext[0]):
                new_entries.append(entry)
            elif ext[1] is None or self.molecule_matches(entry, ext[1]):
                comp_entries.append(entry)
            else:
                logging.error("molecule matched neither the new group or its complement")
                for p, atm in enumerate(parent.item.atoms):
                    if atm.reg_dim_atm[0] != atm.reg_dim_atm[1]:
                        logging.error('atom violation')
                        logging.error(atm.reg_dim_atm)
                        logging.error(parent.label)
                        logging.error('Regularization dimension suggest this node can be expanded, '
                                      'but extension generation has failed')
                    if atm.reg_dim_u[0] != atm.reg_dim_u[1]:
                        logging.error('radical violation')
                        logging.error(atm.reg_dim_u)
                        logging.error(parent.label)
                        logging.error('Regularization dimension suggest this node can be expanded, '
                                      'but extension generation has failed')
                for p, bd in enumerate(parent.item.get_all_edges()):
                    if bd.reg_dim[0] != bd.reg_dim[1]:
                        logging.error('bond violation')
                        logging.error(bd.order)
                        logging.error(bd.reg_dim)
                        logging.error(parent.label)
                        logging.error('Regularization dimension suggest this node can be expanded, '
                                      'but extension generation has failed')

                logging.error('split violation')
                logging.error("proposed")
                logging.error(ext[0].to_adjacency_list())
                if ext[1]:
                    logging.error("proposed complement")
                    logging.error(ext[1].to_adjacency_list())
                logging.error('parent')
                logging.error(parent.item.to_adjacency_list())
                for c, atm in enumerate(parent.item.atoms):
                    logging.error(c)
                    logging.error(atm.reg_dim_atm)
                    logging.error(atm.reg_dim_u)
                logging.error("bonds:")
                for bd in parent.item.get_all_edges():
                    ind1 = parent.item.atoms.index(bd.vertex1)
                    ind2 = parent.item.atoms.index(bd.vertex2)
                    logging.error(((ind1, ind2), bd.order, bd.reg_dim))
                ms = template_mol_map[parent.label]
                for mol in ms:
                    logging.error(str(mol))
                    for react in mol.reactants:
                        logging.error(react.label)
                        logging.error(react.to_adjacency_list())
                    for prod in mol.products:
                        logging.error(prod.label)
                        logging.error(prod.to_adjacency_list())
                raise ValueError
        
        template_mol_map[extname] = new_entries

        if complement:
            template_mol_map[parent.label] = []
            template_mol_map[cextname] = comp_entries
        else:
            template_mol_map[parent.label] = comp_entries
        return (True, None)
    
    def get_extension_edge(self, parent, template_mol_map, obj, Ts, r=None, iteration_max=np.inf, iteration_item_cap=np.inf, use_model_variance_prepruning=False, model_variance_prepruning_threshold=0.05):
        """
        finds the set of all extension groups to parent such that
        1) the extension group divides the set of molecules under parent
        2) No generalization of the extension group divides the set of molecules under parent

        We find this by generating all possible extensions of the initial group.  Extensions that split molecules are added
        to the list.  All extensions that do not split molecules and do not create bonds are ignored 
        (although those that match every molecule are labeled so we don't search them twice).  Those that match
        all molecules and involve bond creation undergo this process again.  

        Principle:  Say you have two elementary changes to a group ext1 and ext2 if applying ext1 and ext2 results in a 
        split at least one of ext1 and ext2 must result in a split

        Speed of this algorithm relies heavily on searching non bond creation dimensions once.
        """
        out_exts = [[]]
        grps = [[parent.item]]
        names = [parent.label]
        first_time = True
        gave_up_split = False

        iteration = 0

        while grps[iteration] != []:
            grp = grps[iteration][-1]

            exts = grp.get_extensions(basename=names[-1],r=r)

            reg_dict = dict()
            ext_inds = []
            for i, (grp2, grpc, name, typ, indc) in enumerate(exts):

                if typ != 'intNewBondExt' and typ != 'extNewBondExt' and (typ, indc) not in reg_dict.keys():
                    # first list is all extensions that match at least one molecule
                    # second is extensions that match all molecules
                    reg_dict[(typ, indc)] = ([], [])
                val, boo = self.eval_ext(parent, grp2, name, template_mol_map, obj=obj, Ts=Ts)

                if val != np.inf:
                    out_exts[-1].append(exts[i])  # this extension splits molecules (optimization dim)
                    if typ == 'atomExt':
                        reg_dict[(typ, indc)][0].extend(grp2.atoms[indc[0]].atomtype)
                    elif typ == 'elExt':
                        reg_dict[(typ, indc)][0].extend(grp2.atoms[indc[0]].radical_electrons)
                    elif typ == 'bondExt':
                        reg_dict[(typ, indc)][0].extend(grp2.get_bond(grp2.atoms[indc[0]], grp2.atoms[indc[1]]).order)

                elif boo:  # this extension matches all molecules (regularization dim)
                    if typ == 'intNewBondExt' or typ == 'extNewBondExt':
                        # these are bond formation extensions, we want to expand these until we get splits
                        ext_inds.append(i)
                    elif typ == 'atomExt':
                        reg_dict[(typ, indc)][0].extend(grp2.atoms[indc[0]].atomtype)
                        reg_dict[(typ, indc)][1].extend(grp2.atoms[indc[0]].atomtype)
                    elif typ == 'elExt':
                        reg_dict[(typ, indc)][0].extend(grp2.atoms[indc[0]].radical_electrons)
                        reg_dict[(typ, indc)][1].extend(grp2.atoms[indc[0]].radical_electrons)
                    elif typ == 'bondExt':
                        reg_dict[(typ, indc)][0].extend(grp2.get_bond(grp2.atoms[indc[0]], grp2.atoms[indc[1]]).order)
                        reg_dict[(typ, indc)][1].extend(grp2.get_bond(grp2.atoms[indc[0]], grp2.atoms[indc[1]]).order)
                    elif typ == 'ringExt':
                        reg_dict[(typ, indc)][1].append(True)
                else:
                    # this extension matches no molecules
                    if typ == 'ringExt':
                        reg_dict[(typ, indc)][0].append(False)
                        reg_dict[(typ, indc)][1].append(False)

            for typr, indcr in reg_dict.keys():  # have to label the regularization dimensions in all relevant groups
                reg_val = reg_dict[(typr, indcr)]

                if first_time and parent.children == []:
                    # parent
                    if typr != 'intNewBondExt' and typr != 'extNewBondExt':  # these dimensions should be regularized
                        if typr == 'atomExt':
                            grp.atoms[indcr[0]].reg_dim_atm = list(reg_val)
                        elif typr == 'elExt':
                            grp.atoms[indcr[0]].reg_dim_u = list(reg_val)
                        elif typr == 'ringExt':
                            grp.atoms[indcr[0]].reg_dim_r = list(reg_val)
                        elif typr == 'bondExt':
                            atms = grp.atoms
                            bd = grp.get_bond(atms[indcr[0]], atms[indcr[1]])
                            bd.reg_dim = list(reg_val)

                # extensions being sent out
                if typr != 'intNewBondExt' and typr != 'extNewBondExt':  # these dimensions should be regularized
                    for grp2, grpc, name, typ, indc in out_exts[-1]:  # returned groups
                        if typr == 'atomExt':
                            grp2.atoms[indcr[0]].reg_dim_atm = list(reg_val)
                            if grpc:
                                grpc.atoms[indcr[0]].reg_dim_atm = list(reg_val)
                        elif typr == 'elExt':
                            grp2.atoms[indcr[0]].reg_dim_u = list(reg_val)
                            if grpc:
                                grpc.atoms[indcr[0]].reg_dim_u = list(reg_val)
                        elif typr == 'ringExt':
                            grp2.atoms[indcr[0]].reg_dim_r = list(reg_val)
                            if grpc:
                                grpc.atoms[indcr[0]].reg_dim_r = list(reg_val)
                        elif typr == 'bondExt':
                            atms = grp2.atoms
                            bd = grp2.get_bond(atms[indcr[0]], atms[indcr[1]])
                            bd.reg_dim = [list(set(bd.order) & set(reg_val[0])), list(set(bd.order) & set(reg_val[1]))]
                            if grpc:
                                atms = grpc.atoms
                                bd = grpc.get_bond(atms[indcr[0]], atms[indcr[1]])
                                bd.reg_dim = [list(set(bd.order) & set(reg_val[0])),
                                              list(set(bd.order) & set(reg_val[1]))]

            # extensions being expanded
            for typr, indcr in reg_dict.keys():  # have to label the regularization dimensions in all relevant groups
                reg_val = reg_dict[(typr, indcr)]
                if typr != 'intNewBondExt' and typr != 'extNewBondExt':  # these dimensions should be regularized
                    for ind2 in ext_inds:  # groups for expansion
                        grp2, grpc, name, typ, indc = exts[ind2]
                        if typr == 'atomExt':
                            grp2.atoms[indcr[0]].reg_dim_atm = list(reg_val)
                            if grpc:
                                grpc.atoms[indcr[0]].reg_dim_atm = list(reg_val)
                        elif typr == 'elExt':
                            grp2.atoms[indcr[0]].reg_dim_u = list(reg_val)
                            if grpc:
                                grpc.atoms[indcr[0]].reg_dim_u = list(reg_val)
                        elif typr == 'ringExt':
                            grp2.atoms[indcr[0]].reg_dim_r = list(reg_val)
                            if grpc:
                                grpc.atoms[indcr[0]].reg_dim_r = list(reg_val)
                        elif typr == 'bondExt':
                            atms = grp2.atoms
                            bd = grp2.get_bond(atms[indcr[0]], atms[indcr[1]])
                            bd.reg_dim = [list(set(bd.order) & set(reg_val[0])), list(set(bd.order) & set(reg_val[1]))]
                            if grpc:
                                atms = grpc.atoms
                                bd = grpc.get_bond(atms[indcr[0]], atms[indcr[1]])
                                bd.reg_dim = [list(set(bd.order) & set(reg_val[0])),
                                              list(set(bd.order) & set(reg_val[1]))]

            out_exts.append([])
            grps[iteration].pop()
            names.pop()

            for ind in ext_inds:  # collect the groups to be expanded
                grpr, grpcr, namer, typr, indcr = exts[ind]
                if len(grps) == iteration+1:
                    grps.append([])
                grps[iteration+1].append(grpr)
                names.append(namer)

            if first_time:
                first_time = False

            if grps[iteration] == [] and len(grps) != iteration+1 and (not (any([len(x)>0 for x in out_exts]) and iteration+1 > iteration_max)):
                iteration += 1
                if len(grps[iteration]) > iteration_item_cap:
                    logging.error("Recursion item cap hit not splitting {0} molecules at iteration {1} with {2} items".format(len(template_mol_map[parent.label]),iteration,len(grps[iteration])))
                    iteration -= 1
                    gave_up_split = True

            elif grps[iteration] == [] and len(grps) != iteration+1 and (any([len(x)>0 for x in out_exts]) and iteration+1 > iteration_max):
                logging.info("iteration_max achieved terminating early")

        out = []
        # compile all of the valid extensions together
        # may be some duplicates here, but I don't think it's Hand-madely worth identifying them
        for x in out_exts:
            out.extend(x)

        return out, gave_up_split

    
    def eval_ext(self, parent, ext, extname, template_mol_map, obj=None, Ts=None):
        """
        evaluates the objective function obj
        for the extension ext with name extname to the parent entry parent
        """
        mols_corrections = template_mol_map[parent.label]
        new, old, new_inds = self._split_molecules(mols_corrections, ext)
        if len(new) == 0:
            return np.inf, False
        elif len(old) == 0:
            return np.inf, True
        else:
            if obj:
                ob, boo = get_objective_function(new, old, obj, Ts=Ts)
            else:
                ob, boo = get_objective_function(new, old, Ts=Ts)
            return ob, True
        
    def _split_molecules(self, mols_corrections, newgrp):
        """
        divides the molecules in mols_corrections between the new
        group structure newgrp and the old structure with 
        label oldlabel
        returns a list of molecules associated with the new group
        the list of molecules associated with the old group
        and a list of the indices of all of the molecules
        associated with the new group
        """
        new = []
        comp = []
        new_inds = []

        for i, mols_corrections in enumerate(mols_corrections):
            mol, correction = mols_corrections
            mol.identify_ring_membership()

            if mol.is_subgraph_isomorphic(newgrp, generate_initial_map=True, save_order=True):
                new.append(mols_corrections)
                new_inds.append(i)
            else:
                comp.append(mols_corrections)

        return new, comp, new_inds
    
    def add_entry(self, parent, grp, name):
        """
        Adds a group entry with parent parent
        group structure grp
        and group name name
        """
        ind = len(self.entries) - 1
        entry = Entry(index=ind, label=name, item=grp, parent=parent)
        self.entries[name] = entry
        if entry.parent:
            entry.parent.children.append(entry)
            
    def molecule_matches(self, mols_corrections, grp):
        mol, correction = mols_corrections
        mol.identify_ring_membership()
        return mol.is_subgraph_isomorphic(grp, generate_initial_map=True, save_order=True)
    
    def save(self, path, reindex=True):
        """
        Save the Hand-made database to the file at location `path` on disk. 
        """
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            pass

        if reindex:
            entries = self.get_entries_to_save()
        else: 
            entries = self.entries.values()

        f = codecs.open(path, 'w', 'utf-8')
        f.write('#!/usr/bin/env python\n')
        f.write('# encoding: utf-8\n\n')
        f.write('name = "{0}"\n'.format(self.name))
        f.write('shortDesc = "{0}"\n'.format(self.short_desc))
        f.write('longDesc = """\n')
        f.write(self.long_desc.strip() + '\n')
        f.write('"""\n')

        for entry in entries:
            self.save_entry(f, entry)

        # Write the tree
        if len(self.top) > 0:
            f.write('tree(\n')
            f.write('"""\n')
            f.write(self.generate_old_tree(self.top, 1))
            f.write('"""\n')
            f.write(')\n\n')

        f.close()

    def generate_old_tree(self, entries, level):
        """
        Generate a multi-line string representation of the Hand-made tree using
        the old-style syntax.
        """
        string = ''
        for entry in entries:
            # Write Hand-made node
            string += '{0}L{1:d}: {2}\n'.format('    ' * (level - 1), level, entry.label)
            # Recursively descend children (depth-first)
            string += self.generate_old_tree(entry.children, level + 1)
        return string

    def prune_tree(self, mols_corrections, newmols_corrections, new_fraction_threshold_to_reopt_node=0.25,
                   exact_matches_only=True, n_jobs=1):
        """
        Remove nodes that have less than maxmolToReoptNode molecules that match
        and clear the regularization dimensions of their parent
        This is used to remove smaller easier to optimize and more likely to change nodes
        before adding a new batch in cascade model generation
        """
        template_mol_map = self.get_molecule_matches(mols_corrections=mols_corrections,
                                                     exact_matches_only=False, n_jobs=n_jobs)
        for key, item in template_mol_map.items():
            entry = self.entries[key]
            parent = entry.parent
            Nmols_corrections = float(len(template_mol_map[entry.label]))
            if parent and Nmols_corrections > 0:
                Nmols_correctionsnew = float(len(set(template_mol_map[entry.label]) & set(newmols_corrections)))
                if Nmols_correctionsnew/Nmols_corrections > new_fraction_threshold_to_reopt_node:
                    parent.children.remove(entry)
                    del self.entries[key]
                else:
                    entry.item.clear_reg_dims()

    def check_tree(self, entry=None):
        if entry is None:
            entry = self.top[0]
        for child in entry.children:
            if not child.item.is_subgraph_isomorphic(entry.item, generate_initial_map=True, save_order=True):
                logging.error('child: ')
                logging.error(child.label)
                logging.error(child.item.to_adjacency_list())
                logging.error('parent: ')
                logging.error(entry.label)
                logging.error(entry.item.to_adjacency_list())
                raise ValueError('Child not subgraph isomorphic to parent')
            self.check_tree(child)
        for entry in self.entries.values():
            if entry.index == -1:
                continue
            parent = entry
            while parent.parent is not None:
                parent = parent.parent
            assert parent.label == 'Root', parent.label
            
    def simple_regularization(self, node, template_mol_map, test=True):
        """
        Simplest regularization algorithm
        All nodes are made as specific as their descendant reactions
        Training reactions are assumed to not generalize 
        For example if an particular atom at a node is Oxygen for all of its
        descendent reactions a reaction where it is Sulfur will never hit that node
        unless it is the top node even if the tree did not split on the identity 
        of that atom
        
        The test option to this function determines whether or not the reactions 
        under a node match the extended group before adding an extension. 
        If the test fails the extension is skipped. 
        
        In general test=True is needed if the cascade algorithm was used 
        to generate the tree and test=False is ok if the cascade algorithm
        wasn't used. 
        """

        for child in node.children:
            self.simple_regularization(child, template_mol_map)

        grp = node.item
        mols_corrections = template_mol_map[node.label]

        all_elements = elements.bde_elements  # set of possible R elements/atoms
        R = [ATOMTYPES[x] for x in all_elements]
        for x in all_elements:
            R.extend(ATOMTYPES[x].specific)

        RnH = R[:]
        RnH.remove(ATOMTYPES['H'])

        Run = [0, 1, 2, 3]

        atm_dict = {'R': R, 'R!H': RnH}

        if isinstance(node.item, Group):
            indistinguishable = []
            for i, atm1 in enumerate(grp.atoms):

                skip = False
                if node.children == []:  # if the atoms or bonds are graphically indistinguishable don't regularize
                    bdpairs = {(atm, tuple(bd.order)) for atm, bd in atm1.bonds.items()}
                    for atm2 in grp.atoms:
                        if atm1 is not atm2 and atm1.atomtype == atm2.atomtype and len(atm1.bonds) == len(atm2.bonds):
                            bdpairs2 = {(atm, tuple(bd.order)) for atm, bd in atm2.bonds.items()}
                            if bdpairs == bdpairs2:
                                skip = True
                                indistinguishable.append(i)

                if not skip and atm1.reg_dim_atm[1] != [] and set(atm1.reg_dim_atm[1]) != set(atm1.atomtype):
                    atyp = atm1.atomtype
                    if len(atyp) == 1 and atyp[0] in R:
                        pass
                    else:
                        if len(atyp) == 1 and atyp[0].label in atm_dict.keys():
                            atyp = atm_dict[atyp[0].label]

                        vals = list(set(atyp) & set(atm1.reg_dim_atm[1]))
                        assert vals != [], 'cannot regularize to empty'
                        if all([set(child.item.atoms[i].atomtype) <= set(vals) for child in node.children]):
                            if not test:
                                atm1.atomtype = vals
                            else:
                                oldvals = atm1.atomtype
                                atm1.atomtype = vals
                                if not self.mols_match_node(node, mols_corrections):
                                    atm1.atomtype = oldvals

                if not skip and atm1.reg_dim_u[1] != [] and set(atm1.reg_dim_u[1]) != set(atm1.radical_electrons):
                    if len(atm1.radical_electrons) == 1:
                        pass
                    else:
                        relist = atm1.radical_electrons
                        if relist == []:
                            relist = Run
                        vals = list(set(relist) & set(atm1.reg_dim_u[1]))
                        assert vals != [], 'cannot regularize to empty'

                        if all([set(child.item.atoms[i].radical_electrons) <= set(vals)
                                if child.item.atoms[i].radical_electrons != [] else False for child in node.children]):
                            if not test:
                                atm1.radical_electrons = vals
                            else:
                                oldvals = atm1.radical_electrons
                                atm1.radical_electrons = vals
                                if not self.mols_match_node(node, mols_corrections):
                                    atm1.radical_electrons = oldvals

                if (not skip and atm1.reg_dim_r[1] != [] and
                        ('inRing' not in atm1.props.keys() or atm1.reg_dim_r[1][0] != atm1.props['inRing'])):
                    if 'inRing' not in atm1.props.keys():
                        if (all(['inRing' in child.item.atoms[i].props.keys() for child in node.children]) and
                                all([child.item.atoms[i].props['inRing'] == atm1.reg_dim_r[1] for child in node.children])):
                            if not test:
                                atm1.props['inRing'] = atm1.reg_dim_r[1][0]
                            else:
                                if 'inRing' in atm1.props.keys():
                                    oldvals = atm1.props['inRing']
                                else:
                                    oldvals = None
                                atm1.props['inRing'] = atm1.reg_dim_r[1][0]
                                if not self.mols_match_node(node, mols_corrections):
                                    if oldvals:
                                        atm1.props['inRing'] = oldvals
                                    else:
                                        del atm1.props['inRing']
                if not skip:
                    for j, atm2 in enumerate(grp.atoms[:i]):
                        if j in indistinguishable:  # skip graphically indistinguishable atoms
                            continue
                        if grp.has_bond(atm1, atm2):
                            bd = grp.get_bond(atm1, atm2)
                            if len(bd.order) == 1:
                                pass
                            else:
                                vals = list(set(bd.order) & set(bd.reg_dim[1]))
                                if vals != [] and all([set(child.item.get_bond(child.item.atoms[i], child.item.atoms[j]).order) <= set(vals) for child in node.children]):
                                    if not test:
                                        bd.order = vals
                                    else:
                                        oldvals = bd.order
                                        bd.order = vals
                                        if not self.mols_match_node(node, mols_corrections):
                                            bd.order = oldvals
    def regularize(self, template_mol_map, regularization=simple_regularization, keep_root=True):
        """
        Regularizes the tree according to the regularization function regularization
        """

        if keep_root:
            for child in self.top[0].children:  # don't regularize the root
                regularization(self, child, template_mol_map)
        else:
            regularization(self, self.top[0], template_mol_map)
    
    def make_correction(self, corrections, weighted=True, bounded=True):
        if corrections:
            return average_thermo_data(corrections, weighted=weighted, bounded=bounded)
        else:
            return None

    def make_corrections_from_template_mol_map(self, template_mol_map, n_jobs=1, weighted=True, bounded=True):

        entries = list(self.entries.values())
        correction_lists = [[correction for _, correction in template_mol_map[entry.label]] for entry in entries]
        
        average_corrections = Parallel(n_jobs=n_jobs, verbose=5, backend='multiprocessing')(delayed(self.make_correction)(corrections, weighted=weighted, bounded=bounded) for corrections in correction_lists)

        for ind, correction in enumerate(average_corrections):
            entry = entries[ind]
            self.entries[entry.label].data = correction
            self.entries[entry.label].short_desc = "Radical correction fitted to {0} radicals".format(len(correction_lists[ind]))
            if entry.children:
                long_desc = "Averaged from children nodes"
            else:
                long_desc = "Derived using the following species:\n"
                for mol, correction in template_mol_map[entry.label]:
                    long_desc += f"{mol.to_smiles()} - {correction.comment}"
                    long_desc += "\n"
            self.entries[entry.label].long_desc = long_desc
            
    def soft_cross_validate(self, template_mol_map, data, folds=5, test_mol_inds=None, iterations=0, random_state=1, ascend=False):
        """
        Perform K-fold cross validation on a pre-trained tree.
        After finding an appropriate node for radical correction estimation,
        it will remove the testing data and re-estimate the radical correction,
        and move up the tree iterations times.  
        Returns a dictionary mapping {mol: [G298_est - G298_lib, H298_est - H298_lib, S298_est - S298_lib]}
        """
        mols_corrections = template_mol_map['Root']
        resonance_radicals, radical_corrections0 = data
        
        if test_mol_inds is None:
            if folds == 0:
                folds = len(mols_corrections)

            kf = KFold(folds, shuffle=True, random_state=random_state)
            kfsplits = kf.split(mols_corrections)
        else:
            kfsplits = [([0, ], [0, ])]

        errors = {}
        handmade_errors = {}
        uncertainties = {}

        for train_index, test_index in kfsplits:

            if test_mol_inds is None:
                mols_corrections_test = [mols_corrections[ind] for ind in test_index]
            else:
                mols_corrections_test = [mols_corrections[ind] for ind in test_mol_inds]

            for mol_correction in mols_corrections_test:
                mol, correction = mol_correction
                mol_ind = resonance_radicals.index(mol)
                correction0 = radical_corrections0[mol_ind]

                entry = self.top[0]

                boo = True
                while boo:  # find the entry it matches
                    for child in entry.children:
                        matched_mols_corrections = template_mol_map[child.label]
                        if any(mol==matched_mol for matched_mol, _ in matched_mols_corrections):
                            entry = child
                            break
                    else:
                        boo = False
                while entry.parent and len(set(template_mol_map[entry.label]) - set(mols_corrections_test)) <= 1:
                    if entry.parent:
                        entry = entry.parent

                for q in range(iterations):
                    if entry.parent:
                        entry = entry.parent

                uncertainties[mol] = [
                    self.entries[entry.label].data.H298.uncertainty_si,
                    self.entries[entry.label].data.S298.uncertainty_si,
                    self.entries[entry.label].data.Cpdata.uncertainty_si,
                ]
                
                if not ascend:
                    corrections_list = list(set(template_mol_map[entry.label]) - set(mols_corrections_test))
                    corrections_list = [correction for _, correction in corrections_list]
                    if corrections_list != []:
                        new_correction = self.make_correction(corrections_list)
                        errors[mol] = [
                            (new_correction.get_free_energy(298)-correction.get_free_energy(298))/1000/4.184,
                            (new_correction.get_enthalpy(298)-correction.get_enthalpy(298))/1000/4.184,
                            (new_correction.get_entropy(298)-correction.get_entropy(298))/4.184,
                        ]
                        handmade_errors[mol] = [
                            (correction0.get_free_energy(298)-correction.get_free_energy(298))/1000/4.184,
                            (correction0.get_enthalpy(298)-correction.get_enthalpy(298))/1000/4.184,
                            (correction0.get_entropy(298)-correction.get_entropy(298))/4.184,
                        ]
                    else:
                        raise ValueError('only one piece of correction information in the tree?')
                else:
                    boo = True
                    corrections_list = list(set(template_mol_map[entry.label]) - set(mols_corrections_test))
                    corrections_list = [correction for _, correction in corrections_list]
                    new_correction = self.make_correction(corrections_list)
                    logging.info("determining fold rate")
                    c = 1
                    while boo:
                        parent = entry.parent 
                        if parent is None:
                            break
                        corrections_list_parent = list(set(template_mol_map[parent.label]) - set(mols_corrections_test))
                        corrections_list_parent = [correction for _, correction in corrections_list_parent]
                        new_correction_parent = self.make_correction(corrections_list_parents)
                        err_parent = abs(new_correction_parent.H298.value_si - new_correction.H298.value_si) + np.sqrt(new_correction_parent.H298.uncertainty.value_si/np.pi)                                    + abs(new_correction_parent.S298.value_si - new_correction.S298.value_si) + np.sqrt(new_correction_parent.S298.uncertainty.value_si/np.pi)                                    + sum(abs(new_correction_parent.Cpdata.value_si - new_correction.Cpdata.value_si) + np.sqrt(new_correction_parent.Cpdata.uncertainty.value_si/np.pi))
                
                        err_entry = np.sqrt(new_correction.H298.uncertainty.value_si/np.pi)                                    + np.sqrt(new_correction.S298.uncertainty.value_si/np.pi)                                    + sum(np.sqrt(new_correction.Cpdata.uncertainty.value_si/np.pi))
                        if err_entry > err_parent:
                            entry = entry.parent
                            new_correction = new_correction_parent
                            logging.error("recursing {}".format(c))
                            c += 1
                        else:
                            boo = False
                            
                    errors[mol] = [
                        (new_correction.get_free_energy(298)-correction.get_free_energy(298))/1000/4.184,
                        (new_correction.get_enthalpy(298)-correction.get_enthalpy(298))/1000/4.184,
                        (new_correction.get_entropy(298)-correction.get_entropy(298))/4.184,
                    ]
                    
        return errors, handmade_errors, uncertainties
    
    def hard_cross_validate(self, mols_corrections, thermo_database, data, folds=5, random_state=1,
                           obj=None, Ts=None, nprocs=1, min_splitable_entry_num=2,
                              min_mols_corrections_to_spawn=20, max_batch_size=800, outlier_fraction=0.02, stratum_num=8,
                              new_fraction_threshold_to_reopt_node=0.25, extension_iteration_max=np.inf, extension_iteration_item_cap=np.inf,
                              min_mols_corrections_to_split=1, n_jobs=1
                           ):
        """
        Perform K-fold cross validation on the full algorithm
        Returns a dictionary mapping {mol: [G298_est - G298_lib, H298_est - H298_lib, S298_est - S298_lib]}
        """
        resonance_radicals, radical_corrections0 = data
        
        kf = KFold(folds, shuffle=True, random_state=random_state)
        kfsplits = kf.split(mols_corrections)

        errors = {}
        handmade_errors = {}

        for train_index, test_index in kfsplits:

            mols_corrections_test = [mols_corrections[ind] for ind in test_index]
            mols_corrections_train = [mols_corrections[ind] for ind in train_index]
            trained_tree = self._train_tree(mols_corrections=mols_corrections_train, obj=obj, Ts=Ts, nprocs=nprocs, min_splitable_entry_num=min_splitable_entry_num,
                             min_mols_corrections_to_spawn=min_mols_corrections_to_spawn, max_batch_size=np.inf, outlier_fraction=outlier_fraction, stratum_num=stratum_num,
                             new_fraction_threshold_to_reopt_node=new_fraction_threshold_to_reopt_node, extension_iteration_max=extension_iteration_max,
                             extension_iteration_item_cap=extension_iteration_item_cap, min_mols_corrections_to_split=min_mols_corrections_to_split, n_jobs=n_jobs)
            for mol_correction in mols_corrections_test:
                mol, correction = mol_correction
                mol_ind = resonance_radicals.index(mol)
                correction0 = radical_corrections0[mol_ind]
                new_correction = thermo_database._add_group_thermo_data(None, trained_tree, mol, {"*": [atom for atom in mol.atoms if atom.radical_electrons==1][0]})[0]
                errors[mol] = [
                    (new_correction.get_free_energy(298)-correction.get_free_energy(298))/1000/4.184,
                    (new_correction.get_enthalpy(298)-correction.get_enthalpy(298))/1000/4.184,
                    (new_correction.get_entropy(298)-correction.get_entropy(298))/4.184,
                ]
                handmade_errors[mol] = [
                    (correction0.get_free_energy(298)-correction.get_free_energy(298))/1000/4.184,
                    (correction0.get_enthalpy(298)-correction.get_enthalpy(298))/1000/4.184,
                    (correction0.get_entropy(298)-correction.get_entropy(298))/4.184,
                ]
                
                    
        return errors, handmade_errors
    
    def _train_tree(self, mols_corrections, obj=None, Ts=None, nprocs=1, min_splitable_entry_num=2,
                      min_mols_corrections_to_spawn=20, max_batch_size=800, outlier_fraction=0.02, stratum_num=8,
                      new_fraction_threshold_to_reopt_node=0.25, extension_iteration_max=np.inf, extension_iteration_item_cap=np.inf,
                      min_mols_corrections_to_split=1, n_jobs=1):
        """
        Helper function for hard cross validation
        """
        #clean tree
        tree = ThermoGroups(label="radical",
                            name="Radical Corrections")

        tree.entries["Root"] = Entry(
            index = 0,
            label = "Root",
            item = Group().from_adjacency_list(f"""1 * R u[1,2,3,4]"""),
            data = None,
            data_count = 0,
            parent = None,
        )
        tree.entries["RJ1"] = Entry(
            index = 0,
            label = "RJ1",
            item = Group().from_adjacency_list(f"""1 * R u1"""),
            data = None,
            data_count = 0,
            parent = tree.entries["Root"],
        )
        tree.entries["Root"].children = [tree.entries["RJ1"]]
        tree.top = [tree.entries["Root"]]

        start = time.time()
        template_mol_map_exact = tree.generate_tree(mols_corrections=mols_corrections, obj=obj, Ts=Ts, nprocs=nprocs, min_splitable_entry_num=min_splitable_entry_num,
                                                    min_mols_corrections_to_spawn=min_mols_corrections_to_spawn, max_batch_size=np.inf, outlier_fraction=outlier_fraction, stratum_num=stratum_num,
                                                    new_fraction_threshold_to_reopt_node=new_fraction_threshold_to_reopt_node, extension_iteration_max=extension_iteration_max,
                                                    extension_iteration_item_cap=extension_iteration_item_cap, min_mols_corrections_to_split=min_mols_corrections_to_split, n_jobs=n_jobs)
        end = time.time()
        print("Tree generation:")
        print(end-start)

        tree.check_tree()

        start = time.time()
        template_mol_map = tree.get_molecule_matches(mols_corrections=mols_corrections,
                                                             exact_matches_only=False, n_jobs=n_jobs)

        end = time.time()
        print("Mol mapping:")
        print(end-start)

        tree.regularize(template_mol_map)

        start = time.time()
        tree.make_corrections_from_template_mol_map(template_mol_map, n_jobs=n_jobs)
        end = time.time()
        print("Make corrections:")
        print(end-start)
        return tree
    
    def hard_cross_validate(self, mols_corrections, thermo_database, data, folds=5, random_state=1,
                           obj=None, Ts=None, nprocs=1, min_splitable_entry_num=2,
                              min_mols_corrections_to_spawn=20, max_batch_size=800, outlier_fraction=0.02, stratum_num=8,
                              new_fraction_threshold_to_reopt_node=0.25, extension_iteration_max=np.inf, extension_iteration_item_cap=np.inf,
                              min_mols_corrections_to_split=1, n_jobs=1
                           ):
        """
        Perform K-fold cross validation on the full algorithm
        Returns a dictionary mapping {mol: [G298_est - G298_lib, H298_est - H298_lib, S298_est - S298_lib]}
        """
        resonance_radicals, radical_corrections0 = data
        
        kf = KFold(folds, shuffle=True, random_state=random_state)
        kfsplits = kf.split(mols_corrections)

        errors = {}
        handmade_errors = {}

        for train_index, test_index in kfsplits:

            mols_corrections_test = [mols_corrections[ind] for ind in test_index]
            mols_corrections_train = [mols_corrections[ind] for ind in train_index]
            trained_tree = self._train_tree(mols_corrections=mols_corrections_train, obj=obj, Ts=Ts, nprocs=nprocs, min_splitable_entry_num=min_splitable_entry_num,
                             min_mols_corrections_to_spawn=min_mols_corrections_to_spawn, max_batch_size=np.inf, outlier_fraction=outlier_fraction, stratum_num=stratum_num,
                             new_fraction_threshold_to_reopt_node=new_fraction_threshold_to_reopt_node, extension_iteration_max=extension_iteration_max,
                             extension_iteration_item_cap=extension_iteration_item_cap, min_mols_corrections_to_split=min_mols_corrections_to_split, n_jobs=n_jobs)
            for mol_correction in mols_corrections_test:
                mol, correction = mol_correction
                mol_ind = resonance_radicals.index(mol)
                correction0 = radical_corrections0[mol_ind]
                new_correction = thermo_database._add_group_thermo_data(None, trained_tree, mol, {"*": [atom for atom in mol.atoms if atom.radical_electrons==1][0]})[0]
                errors[mol] = [
                    (new_correction.get_free_energy(298)-correction.get_free_energy(298))/1000/4.184,
                    (new_correction.get_enthalpy(298)-correction.get_enthalpy(298))/1000/4.184,
                    (new_correction.get_entropy(298)-correction.get_entropy(298))/4.184,
                ]
                handmade_errors[mol] = [
                    (correction0.get_free_energy(298)-correction.get_free_energy(298))/1000/4.184,
                    (correction0.get_enthalpy(298)-correction.get_enthalpy(298))/1000/4.184,
                    (correction0.get_entropy(298)-correction.get_entropy(298))/4.184,
                ]
                
                    
        return errors, handmade_errors
                
    def generate_tree(self, mols_corrections=None, obj=None, Ts=None, nprocs=1, min_splitable_entry_num=2,
                      min_mols_corrections_to_spawn=20, max_batch_size=800, outlier_fraction=0.02, stratum_num=8,
                      new_fraction_threshold_to_reopt_node=0.25, extension_iteration_max=np.inf, extension_iteration_item_cap=np.inf,
                      min_mols_corrections_to_split=1, n_jobs=1,
                      use_aleatoric_prepruning=False, aleatoric_prepruning_function=min,
                      use_model_variance_prepruning=False, model_variance_prepruning_threshold=0.05,
                      ):
        """
        Generate a tree by greedy optimization based on the objective function obj
        the optimization is done by iterationating through every group and if the group has
        more than one training molecule associated with it a set of potential more specific extensions 
        are generated and the extension that optimizing the objective function combination is chosen 
        and the iterationation starts over at the beginning
        
        additionally the tree structure is simplified on the fly by removing groups that have no kinetics data
        associated if their parent has no kinetics data associated and they either have only one child or
        have two children one of which has no kinetics data and no children
        (its parent becomes the parent of its only relevant child node)
        
        Args:
            mols_corrections: List of molecules to generate tree from (if None pull the whole training set)
            obj: Object to expand tree from (if None uses top node)
            thermo_database: Thermodynamic database used for reversing training molecules
            T: Temperature the tree is optimized for
            nprocs: Number of process for parallel tree generation 
            min_splitable_entry_num: the minimum number of splitable molecules at a node in order to spawn
                a new process solving that node
            min_mols_corrections_to_spawn: the minimum number of molecules at a node to spawn a new process solving that node
            max_batch_size: the maximum number of molecules allowed in a batch, most batches will be this size
                the last will be smaller, if the # of molecules < max_batch_size the cascade algorithm is not used
            outlier_fraction: Fraction of molecules that are fastest/slowest and will be automatically included
                in the first batch
            stratum_num: Number of strata used in stratified sampling scheme
            max_mols_corrections_to_reopt_node: Nodes with more matching molecules than this will not be pruned
        """
        if Ts is None:
            Ts = [300, 400, 500, 600, 800, 1000, 1500]
        if mols_corrections is None:
            mols_corrections = self.get_training_set()

        if len(mols_corrections) <= max_batch_size:
            template_mol_map = self.get_molecule_matches(mols_corrections=mols_corrections, exact_matches_only=True, n_jobs=n_jobs)
            self.make_tree_nodes(template_mol_map=template_mol_map, obj=obj, Ts=Ts, nprocs=nprocs - 1, depth=0,
                                 min_splitable_entry_num=min_splitable_entry_num, min_mols_corrections_to_spawn=min_mols_corrections_to_spawn, extension_iteration_max=extension_iteration_max,
                                 min_mols_corrections_to_split=min_mols_corrections_to_split, n_jobs=n_jobs,
                                 use_aleatoric_prepruning=use_aleatoric_prepruning, aleatoric_prepruning_function=aleatoric_prepruning_function,
                                 use_model_variance_prepruning=use_model_variance_prepruning, model_variance_prepruning_threshold=model_variance_prepruning_threshold)
        else:
            def molkey(mol):
                return len(mol.atoms)
            mols_correctionsorted = sorted(mols_corrections, key=molkey)
            batches = [mols_correctionsorted[i * max_batch_size:(i + 1) * max_batch_size] for i in range((len(mols_correctionsorted) + max_batch_size - 1) // max_batch_size )]
            for i, batch in enumerate(batches):
                if i == 0:
                    mols_corrections = batch
                else:
                    mols_corrections += batch
                    logging.error("pruning tree")
                    self.prune_tree(mols_corrections, batch, new_fraction_threshold_to_reopt_node=new_fraction_threshold_to_reopt_node)
                    logging.error("pruned tree down to {} nodes".format(len(list(self.entries))))
                logging.error("getting molecule matches")
                template_mol_map = self.get_molecule_matches(mols_corrections=mols_corrections, exact_matches_only=True,)
                logging.error("building tree with {} mols_corrections".format(len(mols_corrections)))
                self.make_tree_nodes(template_mol_map=template_mol_map, obj=obj, Ts=Ts, nprocs=nprocs - 1, depth=0,
                                     min_splitable_entry_num=min_splitable_entry_num, min_mols_corrections_to_spawn=min_mols_corrections_to_spawn, extension_iteration_max=extension_iteration_max,
                                     min_mols_corrections_to_split=min_mols_corrections_to_split, n_jobs=n_jobs)
                logging.error("built tree with {} nodes".format(len(list(self.entries))))
            
        def get_data_count(entry):

            data_count = len(template_mol_map[entry.label])

            for child in entry.children:
                data_count += get_data_count(child)
            return data_count

        for entry in self.entries.values():
            entry.data_count = get_data_count(entry)
            
        return template_mol_map
#         self.auto_generated = True
        
def split(corrections1, corrections2):
    """
    calculates the information gain as the sum of the products of the standard deviations at each
    node and the number of molecules at that node
    """
    return abs(len(corrections1)-len(corrections2))

def information_gain(corrections1, corrections2, Ts):
    """
    calculates the information gain as the sum of the products of the standard deviations at each
    node and the number of reactions at that node
    """

    if corrections2:
        Gs1_Ts = [np.array([correction.get_free_energy(T) for correction in corrections1]) for T in Ts]
        Gs2_Ts = [np.array([correction.get_free_energy(T) for correction in corrections2]) for T in Ts]
        
        return len(corrections1) * sum(np.std(Gs_T) for Gs_T in Gs1_Ts) + len(corrections2) * sum(np.std(Gs_T) for Gs_T in Gs2_Ts)
    else:
        Gs1_Ts = [np.array([correction.get_free_energy(T) for correction in corrections1]) for T in Ts]
        return len(corrections1) * sum(np.std(Gs_T) for Gs_T in Gs1_Ts)


def get_objective_function(mols_corrections_1, mols_corrections_2, obj=information_gain, Ts=None):
    """
    Returns the value of four potential objective functions to minimize
    Uncertainty = N1*std(Ln(k))_1 + N1*std(Ln(k))_1
    Mean difference: -abs(mean(Ln(k))_1-mean(Ln(k))_2)
    Error using mean: Err_1 + Err_2
    Split: abs(N1-N2)
    """
    corrections1 = [correction for mol, correction in mols_corrections_1]
    corrections2 = [correction for mol, correction in mols_corrections_2]
    N1 = len(corrections1)

    return obj(corrections1, corrections2, Ts=Ts), N1 == 0
