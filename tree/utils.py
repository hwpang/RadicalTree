import math

from rmgpy import constants
from rmgpy.data.thermo import ThermoData, ThermoDatabase, ThermoLibrary
from rmgpy.molecule import Molecule
from rmgpy.species import Species

linestyles = ['-', '--', '-.', ':']
markers = ['o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H', 'D', 'd']

def load_thermo_lib_by_path(path: str,
                            thermo_db: ThermoDatabase,
                            reload: bool = False):
    """
    Load thermo library given its library path and store it into
    the given RMG ThermoDatabase instance

    Args:
        path (str): Path to thermo library file
        thermo_database (ThermoDatabase): RMG thermo database object
        reload (bool): Whether to reload the library if this library is in the ThermoDatabase
    """
    lib = ThermoLibrary()
    try:
        lib.load(path,
                 ThermoDatabase().local_context,
                 ThermoDatabase().global_context)
    except FileNotFoundError:
        print(f'The library file {path} does not exist.')
    except (SyntaxError, ImportError):
        print(f'The library file {path} is not valid.')
    else:
        if path in thermo_db.library_order and not reload:
            print(f'The library {path} has already been loaded.')
            return
        elif path not in thermo_db.library_order:
            thermo_db.library_order.append(path)
        lib.label = path
        lib.name = path
        thermo_db.libraries[lib.label] = lib
        print(f'The thermodynamics library {path} is loaded.')

def generate_thermo(thermo_database, smi, resonance=True):
    spc = Species().from_smiles(smi)
    if resonance:
        spc.generate_resonance_structures()
    thermo = thermo_database.get_thermo_data(spc)
    thermo = thermo.to_thermo_data() if not isinstance(thermo, ThermoData) else thermo
    return thermo.H298.value_si/4184, thermo.S298.value_si/4.184, thermo.Cpdata.value_si/4.184, (thermo.S298.value_si + constants.R * math.log(spc.get_symmetry_number()))/4.184, thermo.comment

def make_mol(smi, label=False):
    mol = Molecule().from_smiles(smi)
    if label:
        for atom in mol.atoms:
            if atom.radical_electrons > 0:
                atom.label = "*"
        return mol
    else:
        return mol
