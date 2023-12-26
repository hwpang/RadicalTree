#!/bin/bash -l
#SBATCH -n 1
#SBATCH -N 1

conda activate rmg_rdmc_env_20230623_v2

save_dir=models/split-cluster_run-aleatoric_prepruning-upper_bound

data_path=data/hbi_unc.csv
split_path=data/splits/cluster.json

start_time=$(date +%s)
python train.py \
--save_dir $save_dir \
--data_path $data_path \
--split_path $split_path \
--use_upper_bound_uncertainty \
--use_aleatoric_prepruning
end_time=$(date +%s)
echo "Training time: $((end_time - start_time)) seconds"

start_time=$(date +%s)
python predict.py \
--save_dir $save_dir \
--data_path $data_path \
--split_path $split_path \
--model_path $save_dir/tree.py
end_time=$(date +%s)
echo "Prediction time: $((end_time - start_time)) seconds"
