TRANSFORMERS_OFFLINE=1 \
python ate.py \
--num_train_epochs 3 \
--learning_rate 3e-5 \
--eval_batch_size 16 \
--bert_model 'bert-base-multilingual-uncased' \
--data_dir 'data/' \
--output_dir 'seq_ate/' \
--bestmodel 'best_ate/' \
--max_seq_length 80 \
--do_eval \
--do_train
