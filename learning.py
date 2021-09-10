import pandas as pd
import numpy as np
import pdb

df = pd.read_csv('data.csv',header=None)
maxQ = df.stack().max()
max_indices = df[df==maxQ].stack().index.tolist()
max_idx_s = [idx[0] for idx in max_indices]
max_idx_a = [idx[1] for idx in max_indices]
# pdb.set_trace()
num_a = 5
num_s = 10



