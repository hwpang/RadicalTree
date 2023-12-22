import sys

sys.path.insert(0,"/home/gridsan/hwpang/Software/RMG-Py/")

import argparse
import json
import os
import time as time
from pathlib import Path

import numpy as np
import pandas as pd
from rmgpy.data.base import Entry
from rmgpy.data.thermo import ThermoData
from rmgpy.molecule.group import Group

from tree.parameters import Ts
from tree.thermo import ThermoGroups
from tree.utils import make_mol

parser = argparse.ArgumentParser()
parser.add_argument("--n_jobs", type=int, default=1)
parser.add_argument("--save_dir", type=str)
parser.add_argument("--data_path", type=str)
parser.add_argument("--split_path", type=str)
parser.add_argument("--fraction_training_data", type=float, default=1.0)
parser.add_argument("--random_state", type=int, default=0)
parser.add_argument("--use_aleatoric_prepruning", action="store_true")
parser.add_argument("--use_upper_bound_uncertainty", action="store_true")
parser.add_argument("--use_model_variance_prepruning", action="store_true")
parser.add_argument("--model_variance_prepruning_threshold", type=float, default=0.05)

args = parser.parse_args()

args.save_dir = Path(args.save_dir)
args.data_path = Path(args.data_path)
args.split_path = Path(args.split_path)

n_jobs = args.n_jobs
save_dir = args.save_dir
save_dir.mkdir(exist_ok=True)
data_path = args.data_path
split_path = args.split_path
fraction_training_data = args.fraction_training_data
random_state = args.random_state
use_aleatoric_prepruning = args.use_aleatoric_prepruning
use_upper_bound_uncertainty = args.use_upper_bound_uncertainty
use_model_variance_prepruning = args.use_model_variance_prepruning
model_variance_prepruning_threshold = args.model_variance_prepruning_threshold


# Get data


hbi_unc_df = pd.read_csv(data_path)
hbi_unc_df


with open(split_path, "r") as f:
    train_inds, test_inds = json.load(f)


train_df = hbi_unc_df.loc[train_inds, :]
train_df = train_df.sample(frac=fraction_training_data, random_state=random_state)


mols = train_df["resonance_radical_smiles"].apply(lambda x: make_mol(x, label=True))
mols = mols.to_list()


HBI_corrections = train_df.apply(lambda x: ThermoData(
    H298=(x["HBI_H298 (kcal/mol)"], "kcal/mol", "+|-", x["unc_HBI_H298 (kcal/mol)"]),
    S298=(x["HBI_Sint298 (cal/mol/K)"], "cal/mol/K", "+|-", x["unc_HBI_Sint298 (cal/mol/K)"]),
    Cpdata=([x[f"HBI_Cp{T} (cal/mol/K)"] for T in Ts], "cal/mol/K", "+|-", [x[f"unc_HBI_Cp{T} (cal/mol/K)"] for T in Ts]),
    Tdata=(Ts, "K"),
    comment=f"Radical thermo from {x['radical_source']} and closed shell thermo from {x['closed_shell_thermo_source'].replace('Thermo library: ../data/', '')}"
), axis=1)
HBI_corrections = HBI_corrections.to_list()


mols_corrections = list(zip(mols, HBI_corrections))


# Generate tree

os.makedirs(save_dir, exist_ok=True)


#clean tree
tree = ThermoGroups(
    label="radical",
    name="HBI correction",
)

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
template_mol_map_exact = tree.generate_tree(mols_corrections=mols_corrections, obj=None, Ts=None, nprocs=1, min_splitable_entry_num=2,
                                          min_mols_corrections_to_spawn=20, max_batch_size=np.inf, outlier_fraction=0.02, stratum_num=8,
                                          new_fraction_threshold_to_reopt_node=0.25, extension_iteration_max=2, extension_iteration_item_cap=100, 
                                            min_mols_corrections_to_split=1, n_jobs=n_jobs,
                                            use_aleatoric_prepruning=use_aleatoric_prepruning, use_model_variance_prepruning=use_model_variance_prepruning, model_variance_prepruning_threshold=model_variance_prepruning_threshold)
end = time.time()
print("Tree generation took ", end-start, " seconds")

tree.check_tree()

start = time.time()
template_mol_map = tree.get_molecule_matches(mols_corrections=mols_corrections,
                                                     exact_matches_only=False, n_jobs=n_jobs)
end = time.time()
print("Mol mapping took ", end-start, " seconds")

tree.regularize(template_mol_map)

start = time.time()
tree.make_corrections_from_template_mol_map(template_mol_map, n_jobs=n_jobs, upper_bound=use_upper_bound_uncertainty)
end = time.time()
print("Make corrections took ", end-start, " seconds")

tree.check_tree()

tree.save(save_dir / "tree.py")





