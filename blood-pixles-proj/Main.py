# THIS IS THE MAIN FILE #
# This file will focus on updating the screen

# --- IMPORTS --- #
import pygame
import os # used to load image files in "image-files"
import random # used to RNG update order
import time # debug timers


# --- SETUP VARIABLES --- #
# Game setup
gameGrid = [ # represents game grid. 0 represents an empty position.
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
]

# 0 - empty, 1 - melee, 2 - ranged, 3 - special
player1Cards = [0, 0, 0]
player2Cards = [0, 0, 0]
def drawCards(cardSet):
    for i in range(len(cardSet)):
        cardSet[i] = random.randint(1, 3)

# Window setup
pygame.init()
windowWidth = 1280
windowHeight = 720
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
running = True

# get background image path
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'image-files', 'background.jpg')
# load image
background_image = pygame.image.load(image_path).convert_alpha()
# Scale the image to fit the screen size
background_image = pygame.transform.scale(background_image, (windowWidth, windowHeight))

# arrays for sprite sets
def makeSprites(type):
    image_folder_path = os.path.join(current_dir, 'image-files', type) # pulls correct image folder path
    
    # put images into spriteSet array for animation
    spriteSet = [pygame.image.load(os.path.join(image_folder_path, '0_stand.png')),
                    # pygame.image.load(os.path.join(image_folder_path, '1_walk1.png')),
                    # pygame.image.load(os.path.join(image_folder_path, '2_walk2.png')),
                #pygame.image.load(os.path.join(image_folder_path, '3_attack.png'))]
                ]
    
    return spriteSet
# make sprite sheets
p1RangedSprites = makeSprites("p1Ranged") 
p1MeleeSprites = makeSprites("p1Melee") 
p1SpecialSprites = makeSprites("p1Special") 

p2RangedSprites = makeSprites("p2Ranged") 
p2MeleeSprites = makeSprites("p2Melee") 
p2SpecialSprites = makeSprites("p2Special") 

# --- HELPER FUNCTIONS --- #

# returns center of pixel of grid square
# (chat GPT FTW)
def getTrueCoord(row, guy, gameGrid):
    tile_size=108
    screen_width=windowWidth
    screen_height=windowHeight
    # grid offsets
    cols = 6
    rows = 5
    grid_width = cols * tile_size
    grid_height = rows * tile_size

    offset_x = (screen_width - grid_width) // 2
    offset_y = 0  # aligned to top

    # find grid position
    row_index = gameGrid.index(row)
    col_index = row.index(guy)

    # compute pixel coordinates for center of the cell
    x = offset_x + col_index * tile_size + tile_size // 2
    y = offset_y + row_index * tile_size + tile_size // 2

    return x, y

def drawBasics(notThisGuy = -1):
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    # load in background
    screen.blit(background_image, (0, 0))
    # draw Guys
    # ~ 108 x 108 pixel square
    for row in gameGrid:
        for guy in row:
            if guy != 0:
                if guy.guyNum == notThisGuy:
                    continue
                else:
                    x, y = getTrueCoord(row, guy, gameGrid)
                    image = guy.sprites[0] # "standing" sprite
                    rect = image.get_rect()
                    rect.center = (x, y)
                    screen.blit(guy.sprites[0], (x,y))
    pygame.display.flip()
    return

def animateAction(guy, mode, detail, x, y):
    '''
    x, y = getTrueCoord(x, y)

    if(mode == "attack"):
        drawBasics(guy.guyNum)
        image = guy.sprites[3] # "attacking" sprite
        rect = image.get_rect()
        rect.center = (x, y)
        screen.blit(image, (x,y))

        time.sleep(1)

        drawBasics(guy.guyNum)
        image = guy.sprites[0] # "standing" sprite
        rect = image.get_rect()
        x, y = getTrueCoord(x, y, gameGrid)
        rect.center = (x, y)
        screen.blit(image, (x,y))

        gameGrid[x][y] = 0
        gameGrid

        print()

    if(mode == "move"):
        image = guy.sprites[2] #starts on 2 so it switches and animates starting at 1
        FRAMES = 10 # frames to animate for
        i = FRAMES
        while (i < 108):
            drawBasics(guy.guyNum)
            # switch image
            if image == guy.sprites[1]:
                image = guy.sprites[2]
            elif image == guy.sprites[2]:
                image = guy.sprites[1]
            #update this somehow
            if detail == "up":
                screen.blit(image, x, y+i)
            elif detail == "down":
                screen.blit(image, x, y-i)
            elif detail == "left":
                screen.blit(image, x-i, y)
            elif detail == "right":
                screen.blit(image, x+i, y)
            i = i - (108/FRAMES)

            pygame.display.flip()
            '''
    return

# --- MAIN LOOP --- #
running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # user input turn
    player = 1
    while(player > 0):

        drawBasics() # draw background, draw Guy positions

        if player == 1:
            print("Main.py: Player 1's turn.")
            # player 1 setup
            drawCards(player1Cards)
            print("Main.py: P1 drew the cards:")
            for card in player1Cards:
                print(card)
            # blank right half of screen
            pygame.draw.rect(screen, "black", (windowWidth/2, 0, windowWidth/2, windowHeight))
            # pull up P1 cards
        
        if player == 2:
            print("Main.py: Player 2's turn.")
            # player 2 setup
            drawCards(player2Cards)
            print("Main.py: P2 drew the cards:")
            for card in player2Cards:
                print(card)
            # blank left half of screen
            pygame.draw.rect(screen, "black", (0, 0, windowWidth/2, windowHeight))
            # pull up P2 cards

        ## EVENTS ##
        # pick / place cards loop
            # update guy.player

        pygame.display.flip()
        
        # do stuff with cards
        time.sleep(2) # DEBUG: simulate "decision time" of players

        # END OF TURN
        if player == 1:
            # blank whole screen
            # prompt for P2
            player = 2

        else: # player 2
            # exit while loop
            player = -1
            break

    print("Main.py: left the player-turns loop!")
    print("Main.py: running Guy logic.")
    # run game logic
    positionsUpdated = 0
    updateTracker = [ #array to make sure every guy gets updated, even at random
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0]
    ]

    while (positionsUpdated < (5*6)):
        # view random position
        x = random.randint(0, 4)
        y = random.randint(0, 5)

        while(updateTracker[x][y] == 1): # if grid square has already been updated, generate new position
            x = random.randint(0, 4)
            y = random.randint(0, 5)
        
        if(gameGrid[x][y] != 0): # there is a guy at x, y
            mode, detail = (gameGrid[x][y]).decision() # returns "move" or "attack" and target_pos
            animateAction(gameGrid[x][y], mode, detail, x, y)
            drawBasics()
            print("Main.py: Updated on Guy at x, y: " + str(x) + str(y))
            time.sleep(0.1) # simulate guy update/animation time

        updateTracker[x][y] = 1 # mark grid square as updated
        positionsUpdated += 1

    print("Main.py: end of 'running' loop.")
    drawBasics()

    time.sleep(2) # DEBUG

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()