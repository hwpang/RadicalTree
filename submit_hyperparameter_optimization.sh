#!/bin/bash -l
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --array=0-3

conda activate rmg_rdmc_env_20230623_v2

# lambdas=(0.0005 0.001 0.002 0.005 0.01 0.02 0.05)
# lambdas=(0.00005 0.0001 0.0002)
lambdas=(0.0006 0.0007 0.0008 0.0009)
lambda=${lambdas[$SLURM_ARRAY_TASK_ID]}

split=random_val

save_dir=models/split-${split}_run-model_variance_prepruning_hyperparam_opt-upper_bound/lambda-$lambda
mkdir -p $save_dir

data_path=data/hbi_unc.csv
split_path=data/splits/$split.json

start_time=$(date +%s)
python train.py \
--save_dir $save_dir \
--data_path $data_path \
--split_path $split_path \
--use_upper_bound_uncertainty \
--use_model_variance_prepruning \
--model_variance_prepruning_threshold $lambda
end_time=$(date +%s)
echo "Training time: $((end_time - start_time)) seconds"

start_time=$(date +%s)
python predict.py \
--save_dir $save_dir \
--data_path $data_path \
--split_path $split_path \
--model_path $save_dir/tree.py \
--validation
end_time=$(date +%s)
echo "Prediction time: $((end_time - start_time)) seconds"
