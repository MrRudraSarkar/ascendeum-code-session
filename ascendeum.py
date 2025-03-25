import random
from collections import deque

def game(n: int):
    grid = n*n
    players = deque(i for i in range(1, 4))
    pos_hist = {}
    roll_hist = {}
    winner = None
    
    for i in players:
        pos_hist[i] = []
        roll_hist[i] = []
    
    while players:
        current_player = players.popleft()
        roll = random.randint(1, 6)

        roll_hist[current_player].append(roll)
        
        if pos_hist[current_player]:
            updated_position = pos_hist[current_player][-1] + roll
        else:
            updated_position = roll

        
        if pos_hist[current_player]:
            for i in pos_hist:
                if updated_position == pos_hist[i][-1]:
                    pos_hist[i].append(0)

        if updated_position == grid:
            pos_hist[current_player].append(updated_position)
            winner = current_player
            break
        elif updated_position > grid:
            pos_hist[current_player].append(updated_position-roll)
        else:
            pos_hist[current_player].append(updated_position)

        players.append(current_player)
    
    print(roll_hist)
    print(pos_hist)
    print(f"Winner is: Player {winner}")



print(game(5))

