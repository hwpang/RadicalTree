
# Predict


import sys

sys.path.insert(0,"/home/gridsan/hwpang/Software/RMG-Py/")

import argparse
import json
from pathlib import Path

import pandas as pd
from rmgpy.data.thermo import ThermoDatabase, ThermoGroups
from tqdm import tqdm

from tree.parameters import Ts
from tree.thermo import ThermoGroups as SIDTThermoGroups
from tree.utils import make_mol

parser = argparse.ArgumentParser()
parser.add_argument("--n_jobs", type=int, default=1)
parser.add_argument("--save_dir", type=str)
parser.add_argument("--data_path", type=str)
parser.add_argument("--split_path", type=str)
parser.add_argument("--model_path", type=str)

args = parser.parse_args()

args.save_dir = Path(args.save_dir)
args.data_path = Path(args.data_path)
args.split_path = Path(args.split_path)

n_jobs = args.n_jobs
save_dir = args.save_dir
save_dir.mkdir(exist_ok=True)
data_path = args.data_path
split_path = args.split_path
model_path = args.model_path


# Load test data


hbi_unc_df = pd.read_csv(data_path)


with open(split_path, "r") as f:
    train_inds, test_inds = json.load(f)


test_df = hbi_unc_df.loc[test_inds, :]
test_df


mols = test_df["resonance_radical_smiles"].apply(make_mol)
mols = mols.to_list()


# Load thermo database


def make_prediction(thermo_database, tree, mol):
    atoms = {"*": atom for atom in mol.atoms if atom.radical_electrons==1}
    return thermo_database._add_group_thermo_data(None, tree, mol, atoms)[0]


thermo_database = ThermoDatabase()


# Predict with SIDT tree


sidt_tree = SIDTThermoGroups().load(model_path, thermo_database.local_context, thermo_database.global_context)


thermos = [make_prediction(thermo_database, sidt_tree, mol) for mol in tqdm(mols)]


test_result_df = test_df[["resonance_radical_smiles"]]
test_result_df["HBI_H298 (kcal/mol)"] = [thermo.H298.value_si/4184 for thermo in thermos]
test_result_df["unc_HBI_H298 (kcal/mol)"] = [thermo.H298.uncertainty_si/4184 for thermo in thermos]
test_result_df["HBI_Sint298 (cal/mol/K)"] = [thermo.S298.value_si/4.184 for thermo in thermos]
test_result_df["unc_HBI_Sint298 (cal/mol/K)"] = [thermo.S298.uncertainty_si/4.184 for thermo in thermos]
for i, T in enumerate(Ts):
    test_result_df[f"HBI_Cp{T} (cal/mol/K)"] = [thermo.Cpdata.value_si[i]/4.184 for thermo in thermos]
    test_result_df[f"unc_HBI_Cp{T} (cal/mol/K)"] = [thermo.Cpdata.uncertainty_si[i]/4.184 for thermo in thermos]
test_result_df["comment"] = [thermo.comment for thermo in thermos]


test_result_df.to_csv(save_dir / "test.csv", index=False)





