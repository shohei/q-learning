import numpy as np
from maze import Maze

x_size = 10
y_size = 9

if __name__=="__main__":
    maze = Maze(x_size, y_size)
    map = maze.map
    number = maze.number

    x = 1
    y = 1
    # Right
    a = 0
    x, y, s2 = maze.move(a, x, y, x_size)
    print("x=",x,"y=",y,"s2=",s2)
    # Down
    a = 1
    x, y, s2 = maze.move(a, x, y, x_size)
    print("x=",x,"y=",y,"s2=",s2)
    # Left 
    a = 2
    x, y, s2 = maze.move(a, x, y, x_size)
    print("x=",x,"y=",y,"s2=",s2)
    # Up 
    a = 3
    x, y, s2 = maze.move(a, x, y, x_size)
    print("x=",x,"y=",y,"s2=",s2)


    print(map)
    print(number)
    maze.plot(x_size, y_size)
    input('Press enter to exit.')
