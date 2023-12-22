#!/bin/bash -l
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --array=0

conda activate rmg_rdmc_env_20230623_v2

fractions=(0.001)
frac=${fractions[$SLURM_ARRAY_TASK_ID]}

# save_dir=models/split-random_run-model_variance_prepruning_0.001-upper_bound/frac-$frac
save_dir=models/split-random_run-aleatoric_prepruning-model_variance_prepruning_0.005-upper_bound/frac-$frac
mkdir -p $save_dir

data_path=data/hbi_unc.csv
split_path=data/splits/random.json

start_time=$(date +%s)
python train.py \
--save_dir $save_dir \
--data_path $data_path \
--split_path $split_path \
--fraction_training_data $frac \
--use_upper_bound_uncertainty \
--use_model_variance_prepruning \
--model_variance_prepruning_threshold 0.005 \
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
