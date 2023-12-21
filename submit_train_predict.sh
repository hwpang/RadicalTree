#!/bin/bash -l
#SBATCH -n 4
#SBATCH -N 1

conda activate rmg_rdmc_env_20230623_v2

save_dir=models/split-random_run-basecase

n_jobs=4
data_path=data/hbi_unc.csv
split_path=data/splits/random.json

start_time=$(date +%s)
python train.py \
--save_dir $save_dir \
--n_jobs $n_jobs \
--data_path $data_path \
--split_path $split_path
end_time=$(date +%s)
echo "Training time: $((end_time - start_time)) seconds"

start_time=$(date +%s)
python predict.py \
--save_dir $save_dir \
--n_jobs $n_jobs \
--data_path $data_path \
--split_path $split_path \
--model_path $save_dir/tree.py
end_time=$(date +%s)
echo "Prediction time: $((end_time - start_time)) seconds"
