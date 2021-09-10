import numpy as np
import random


def epsilon_greedy(epsilon, s, num_a, Qtable):
    if epsilon > random.random():
        max_a = random.randint(0,num_a-1)
        maxQ = Qtable[s, max_a]
    else:
        Qtable_s = Qtable[s,:]
        maxQ = Qtable_s.max()
        max_as = np.where(Qtable_s==maxQ)[0].tolist()
        max_a = random.choice(max_as)
    return maxQ, max_a 

num_a = 5
num_s = 10
Qtable = np.zeros((num_s,num_a))

Qtable[3][1] = 9
# Qtable[4][4] = 9 
# Qtable[5][1] = 9 

for i in range(100):
    epsilon = 0.2
    s = 3
    a = epsilon_greedy(epsilon, s, num_a, Qtable)
    maxQ, a = epsilon_greedy(epsilon, s, num_a, Qtable)
    print("s=",s,"a=",a)

