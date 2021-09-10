import numpy as np
import random

def select_action(s, Qtable):
    Qtable_s = Qtable[s,:]
    maxQ = Qtable_s.max()
    max_as = np.where(Qtable_s==maxQ)[0].tolist()
    max_a = random.choice(max_as)
    return maxQ, max_a 

num_a = 5
num_s = 10
Qtable = np.zeros((num_s,num_a))

Qtable[3][2] = 9
Qtable[4][4] = 9 
Qtable[5][1] = 9 

for s in range(num_s):
    maxQ, a = select_action(s, Qtable)
    print("s=",s,"a=",a)

