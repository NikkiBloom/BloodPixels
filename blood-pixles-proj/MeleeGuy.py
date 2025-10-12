import pygame

class MeleeGuy:
    def __init__(self, team: str):
        self.range=1
        self.team=team
        self.sprite

    def decision(grid, posx, posy):
        reachable=[] # All the grid spaces that MeleeGuy can see
        if (posx>0): reachable.append(grid[posx-1][posy]) # To the left of troop
        if (posx<5): reachable.append(grid[posx+1][posy]) # To the right of troop
        if (posy>0): reachable.append(grid[posx][posy-1]) # Below troop
        if (posy<5): reachable.append(grid[posx][posy+1]) # Above troop

        inRange=False
        attackable=[] # All the enemies that MeleeGuy can see and attack
        for i in reachable:
            if (reachable[i]!=0):
                inRange=True
                attackable.append(reachable[i])

        # Check if anyone is reachable and 
        if (inRange): 
            # Choose who to attack
        # else:
            # Move

