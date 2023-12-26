#!/bin/bash -l
#SBATCH -p xeon-g6-volta
#SBATCH --gres=gpu:volta:1
#SBATCH -n 20
#SBATCH -N 1

conda activate chemprop

save_dir=models/split-random_run-chemprop

data_path=data/hbi_unc.csv
split_path=data/splits/random.json

start_time=$(date +%s)
python -u $CHEMPROP/train.py \
--data_path $data_path \
--dataset_type $dataset_type \
--save_dir $save_dir \
--cache_cutoff $cache_cutoff \
--metric $metric \
--epochs $epochs \
--batch_size $batch_size \
--init_lr $init_lr \
--max_lr $max_lr \
--final_lr $final_lr \
--grad_clip $grad_clip \
--warmup_epochs $warmup_epochs \
--log_frequency $log_frequency \
--split_type $split_type \
--hidden_size $hidden_size \
--number_of_molecules $number_of_molecules \
--depth $depth \
--dropout $dropout \
--activation $activation \
--ffn_num_layers $ffn_num_layers \
--ffn_hidden_size $ffn_hidden_size \
--aggregation $aggregation \
--num_folds $num_folds \
--ensemble_size $ensemble_size \
--bias \
--seed $seed \
--pytorch_seed $pytorch_seed \
--ignore_columns "cluster" \
--num_workers 20
end_time=$(date +%s)
echo "Training time: $((end_time - start_time)) seconds"

start_time=$(date +%s)
python -u $CHEMPROP/predict.py \
--test_path $path_test \
--preds_path $save_dir/test_results.pickle \
--checkpoint_dir $save_dir \
--batch_size $batch_size \
--number_of_molecules $number_of_molecules \
--num_workers 20
end_time=$(date +%s)
echo "Prediction time: $((end_time - start_time)) seconds"
