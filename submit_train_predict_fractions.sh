#!/bin/bash -l
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --array=0-10

conda activate rmg_rdmc_env_20230623_v2

fractions=(0.01 0.05 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9)
frac=${fractions[$SLURM_ARRAY_TASK_ID]}

save_dir=models/split-random_run-basecase/frac-$frac

data_path=data/hbi_unc.csv
split_path=data/splits/random.json

start_time=$(date +%s)
python train.py \
--save_dir $save_dir \
--data_path $data_path \
--split_path $split_path \
--fraction_training_data $frac
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
