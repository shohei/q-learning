import numpy as np
import random
TRIAL_MAX = 100
NONE = 0
SUCCESS = 10
num_a = 2
num_s = 2
epsilon = 0.1
alpha = 0.5
gamma = 0.9

def cheese_machine(s,a):
    global s2
    if a==0: # Press button 1
        s2 = 1-s # Toggle bulb state
        reward = NONE 
    else: # Press button 2
        if s==1: # Bulb is ON
            s2 = s # Bulb maintains current state 
            reward= SUCCESS # Cheese gained
        else:
            s2 = s # Bulb maintains current state 
            reward = NONE # No cheese because power is OFF 
    return reward

def max_Qval(s, Qtable):
    Qtable_s = Qtable[s,:]
    maxQ = Qtable_s.max()
    return maxQ

def epsilon_greedy(epsilon, s, num_a, Qtable):
    if epsilon > random.random():
        a = random.randint(0,num_a-1)
    else:
        Qtable_s = Qtable[s,:]
        maxQ = Qtable_s.max()
        max_as = np.where(Qtable_s==maxQ)[0].tolist()
        a = random.choice(max_as)
    return a 

if __name__=="__main__":
    Qtable = np.zeros((num_s,num_a))
    s = 0
    s2 = 0
    for i in range(TRIAL_MAX):
        a = epsilon_greedy(epsilon, s, num_a, Qtable)
        reward = cheese_machine(s,a)
        Q_max = max_Qval(s2, Qtable)

        Qtable[s][a] = (1-alpha)*Qtable[s][a] + alpha*(reward+gamma*Q_max)
        s = s2
        # if reward>0:
            # print("s=",s,"a=",a)
            # print("success")

    print(Qtable)

