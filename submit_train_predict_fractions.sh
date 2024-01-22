#!/bin/bash -l
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --array=0-11

conda activate rmg_rdmc_env_20230623_v2

fractions=(0.001 0.01 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0)
# fractions=(0.9)

frac=${fractions[$SLURM_ARRAY_TASK_ID]}

split_type=random
model_variance_prepruning_threshold=0.001

split_path=data/splits/$split_type.json

# save_dir=models/split-${split_type}_run-basecase/frac-$frac
# save_dir=models/split-${split_type}_run-basecase-bounded/frac-$frac
# save_dir=models/split-${split_type}_run-aleatoric-prepruning-bounded/frac-$frac
# save_dir=models/split-${split_type}_run-model-variance-prepruning-${model_variance_prepruning_threshold}-bounded/frac-$frac

mkdir -p $save_dir

data_path=data/hbi_unc.csv

start_time=$(date +%s)
python train.py \
--save_dir $save_dir \
--data_path $data_path \
--split_path $split_path \
--fraction_training_data $frac \
--use_bounded_uncertainty \
--use_model_variance_prepruning \
--model_variance_prepruning_threshold $model_variance_prepruning_threshold
# --use_aleatoric_prepruning
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
