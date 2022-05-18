TRANSFORMERS_OFFLINE=1 \
python bert_lap4.py \
--num_train_epochs 3 \
--learning_rate 3e-5 \
--eval_batch_size 16 \
--bert_model 'bert-base-multilingual-uncased' \
--data_dir 'data/' \
--output_dir 'logs_lap4/' \
--task_name 'senti' \
--N 12 \
--train_batch_size 16 \
--max_seq_length 80 \
--do_eval \
--do_train
