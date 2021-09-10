import numpy as np
from maze import Maze
import random

alpha=0.5
gamma=0.9
epsilon=10
x_size=10
y_size=9
x_init=1
y_init=1
num_step=100*10
num_trial=300*10
num_a=4
num_s=x_size*y_size

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
    # Initialize Maze
    maze = Maze(x_size, y_size)
    map = maze.map
    number = maze.number

    # Initialize Q-table
    Qtable = np.zeros((num_s,num_a))
    x = x_init
    y = y_init
    s = maze.xy2s(x, y, x_size)
    scount = 0

    for trial in range(num_trial):
        print("trial:",trial)
        for j in range(num_step):
            a = epsilon_greedy(epsilon, s, num_a, Qtable)
            x, y, s2 = maze.move(a,x,y,x_size)
            reward = map[x][y]
            Q_max = max_Qval(s2, Qtable)
            Qtable[s][a] = (1-alpha)*Qtable[s][a] + alpha*(reward+gamma*Q_max)

            if reward<0:
                # Failure
                x=x_init
                y=y_init
                s=maze.xy2s(x,y,x_size)
                # print('Failure')
                continue
            
            elif reward>0:
                # Treasure found 
                x=x_init
                y=y_init
                s = maze.xy2s(x,y,x_size)
                scount += 1
                print("Success")
                continue
            else:
                # Continue
                s = s2

    print("Success time",scount)
    print(Qtable)
    print(map)
    print(number)
    # maze.plot(x_size, y_size)
    # input('Press enter to exit.')
