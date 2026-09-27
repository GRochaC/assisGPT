import os
import tiktoken
import numpy as np

input_file_path = os.path.join(os.path.dirname(__file__), 'data.txt')

with open(input_file_path, 'r', encoding='utf-8') as f:
    data = f.read()
n = len(data)
print(f"Total characters in dataset: {n}")
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_data_ids = enc.encode_ordinary(train_data)
val_data_ids = enc.encode_ordinary(val_data)

# export to bin files
train_data_ids = np.array(train_data_ids, dtype=np.uint16)
val_data_ids = np.array(val_data_ids, dtype=np.uint16)
train_data_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_data_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

print(f"Prepared dataset with {len(train_data_ids):,} training tokens and {len(val_data_ids):,} validation tokens.")