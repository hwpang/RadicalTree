#!/bin/bash -l
#SBATCH -n 4
#SBATCH -N 1
#SBATCH --array=0-4

conda activate rmg_rdmc_env_20230623_v2

fractions=(0.01 0.2 0.4 0.6 0.8)
frac=${fractions[$SLURM_ARRAY_TASK_ID]}

save_dir=models/split-random_run-basecase/frac-$frac

n_jobs=4
data_path=data/hbi_unc.csv
split_path=data/splits/random.json

python train.py \
--save_dir $save_dir \
--n_jobs $n_jobs \
--data_path $data_path \
--split_path $split_path \
--fraction_training_data $frac

python predict.py \
--save_dir $save_dir \
--n_jobs $n_jobs \
--data_path $data_path \
--split_path $split_path \
--model_path $save_dir/tree.py
