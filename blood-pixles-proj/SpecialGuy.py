HEIGHT = 5
WIDTH = 6

class SpecialGuy:
    def __init__(self, team: str):
        self.range = 0 
        self.team = team
    
    def update(self):
        self.range += 1
        print(f"range increased to {self.range}")

    def decision(self, grid, posx, posy):

        attackable = []

        for dx in range(-self.range, self.range + 1):
            remaining_range = self.range - abs(dx)
            for dy in range(-remaining_range, remaining_range + 1):
                
                # Skip  own tile
                if dx == 0 and dy == 0:
                    continue

                nx, ny = posx + dx, posy + dy

                # Check if the target is on the board
                if 0 <= ny < HEIGHT and 0 <= nx < WIDTH:
                    target = grid[ny][nx]
                    if target != 0 and target.team != self.team:
                        dist = abs(dx) + abs(dy)
                        attackable.append({'pos': (nx, ny), 'dist': dist})
        
        if attackable:
            # Find the closest enemy to attack
            close = min(attackable, key=lambda e: e['dist'])
            target_pos = close['pos']
            print(f"SpecialGuy at ({posx}, {posy}) attacking closest enemy at {target_pos}")
            return "attack", target_pos
        else:
            # No enemies 
            print(f"SpecialGuy at ({posx}, {posy}) is moving.")
            return "move", None
