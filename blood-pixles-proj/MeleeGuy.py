# Connor

import pygame
import random

class MeleeGuy:
    def __init__(self, team: str):
        self.guy_type = "melee"
        self.player = 1 # default; update to "2" if necessary in main.py
        self.range=1
        self.team=team
        self.sprites = [] # update in main.py
        self.guyNum = 0 # 0 by default; update in main.py
        self.wonder_directionx = "right" # Internal variable used for decision() logic

    def decision(self, grid, posx, posy):
        reachable=[] # All the grid spaces that MeleeGuy can see
        if (posx>0): reachable.append(grid[posy][posx-1]) # To the left of troop
        if (posx<5): reachable.append(grid[posy][posx+1]) # To the right of troop
        if (posy>0): reachable.append(grid[posy-1][posx]) # Above troop
        if (posy<5): reachable.append(grid[posy+1][posx]) # Below troop

        inRange=False
        attackable=[] # All the enemies that MeleeGuy can see and attack
        for i in reachable:
            if (reachable[i]!=0 and reachable[i].team!=self.team):
                inRange=True
                attackable.append(reachable[i])

        # Check if any enemy is reachable...
        if (inRange): 
            # Choose who to attack
            attacking=random.choice(attackable)
            if (attacking==(grid[posy][posx+1])):
                print("Melee guy at ({posx}, {posy}): ATTACKing Right")
                return "right"
            elif (attacking==(grid[posy][posx-1])):
                print("Melee guy at ({posx}, {posy}): ATTACKing Left")
                return "left"
            elif (attacking==(grid[posy+1][posx])):
                print("Melee guy at ({posx}, {posy}): ATTACKing Down")
                return "down"
            elif (attacking==(grid[posy-1][posx])):
                print("Melee guy at ({posx}, {posy}): ATTACKing Up")
                return "up"
            else:
                print("Melee guy at ({posx}, {posy}) has incorrect ATTACK logic: Defaulting to Right")
                return "right"
        
        # Otherwise move
        else:
            potential_target = 0
            pt_x = 0
            pt_y = 0
            for y in range(5):
                for x in range(6):
                    if (grid[y][x]!=0):
                        if (i.team!=self.team):
                            potential_target = i
                            pt_x = x
                            pt_y = y
                            break
            if (posx==6): # If self is at the end of either side of the stage, flip wonder direction
                    self.wonder_directionx = "left" 
            else:
                self.wonder_directionx = "right"
            if (potential_target!=0):
                if (pt_x>posx and (posx+1)==0):
                    print("Melee guy at ({posx}, {posy}): MOVING Right")
                    return "right"
                elif (pt_y<posx and (posx-1)==0):
                    print("Melee guy at ({posx}, {posy}): MOVING Left")
                    return "left"
                else:
                    if (pt_y<posy and (posy-1)==0):
                        print("Melee guy at ({posx}, {posy}): MOVING Up")
                        return "up"
                    elif (pt_y>posy and (posy+1)==0):
                        print("Melee guy at ({posx}, {posy}): MOVING Down")
                        return "down"
                    else:
                        print("Melee guy at ({posx}, {posy}) is trapped by an ally. CONSUMING ally to the {self.wonder_directionx} >:)")
                        return self.wonder_directionx
            else:
                print("No potential ENEMY target could be found, defaulting to wonder {self.wonder_directionx}")
                return self.wonder_directionx
