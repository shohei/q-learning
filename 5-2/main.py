import numpy as np
import pandas as pd
import pdb

def max_Qval(s, Qtable):
    Qtable_s = Qtable[s,:]
    maxQ = Qtable_s.max()
    max_as = np.where(Qtable_s==maxQ)[0].tolist()
    return maxQ, max_as 

num_s = 5
num_a = 10
Qtable = np.zeros((num_s,num_a))

Qtable[3][2] = 9
Qtable[3][4] = 6 
max, max_as = max_Qval(3, Qtable)
print("max={}".format(max))
print("a={}".format(max_as))
