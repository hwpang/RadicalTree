#!/bin/bash -l
#SBATCH -n 48

conda activate rmg_rdmc_env_20230623

save_dir=split-random_run-basecase

n_jobs=48
data_path=data/hbi_unc.csv
split_path=data/splits/random.json

python train.py \
--save_dir $save_dir \
--n_jobs $n_jobs \
--data_path $data_path \
--split_path $split_path

python predict.py \
--save_dir $save_dir \
--n_jobs $n_jobs \
--data_path $data_path \
--split_path $split_path \
--model_path $save_dir/tree.py
