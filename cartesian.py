from random import randint
from math import ceil
from collections import deque

def cartesian(n: int):
    grid = n*n
    cart_hist = []
    pos_hist = []
    x=0
    y=0

    while True:
        roll = randint(1,6)

        if pos_hist:
            updated_position = pos_hist[-1] + roll
        else:
            updated_position = roll

        #x = n-(updated_position%n) if y % 2 == 0 else updated_position%n
        x = ((updated_position%n) - 1) if updated_position % n != 0 else n-1
        y = (ceil(updated_position/n))-1 

        cart_hist.append((x, y))

        if updated_position == grid:
            pos_hist.append(updated_position)
            break
        elif updated_position > grid:
            pos_hist.append(updated_position-roll)
        else:
            pos_hist.append(updated_position)

    print(pos_hist)
    print(cart_hist)

cartesian(3)