# Kai
import random

HEIGHT = 5
WIDTH = 6

class RangedGuy:
    def __init__(self, team: str):
        self.guy_type = "ranged"
        self.player = 1 # default; update to "2" if necessary in main.py
        self.range = 2
        self.sprites = [] # update in main.py
        self.guyNum = 0 # 0 by default; assign random ID in main.py
       
    # Makes decision for the Guy. Returns "attack" and target_pos OR "move" and none.
    def decision(self, grid, posx, posy):
     
        attackable = []
        
        reachable = [
            (posx - 2, posy), (posx + 2, posy),  # Horizontal
            (posx, posy - 2), (posx, posy + 2),  # Vertical
            (posx - 1, posy - 1), (posx - 1, posy + 1),  # Diagonals
            (posx + 1, posy - 1), (posx + 1, posy + 1)   # Diagonals
        ]

       
        for nx, ny in reachable:
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                target = grid[nx][ny]
                # Check if there is an enemy at that spot
                if target != 0 and target.team != self.team:
                    attackable.append((nx, ny))
        
        if attackable:
            target_pos = random.choice(attackable)
            print(f"RangedGuy at ({posx}, {posy}) attacking{target_pos}")
            return "attack", target_pos
        else:
            # No enemies 
            print(f"Moving to ({posx}, {posy})")
            return "move", "left"
