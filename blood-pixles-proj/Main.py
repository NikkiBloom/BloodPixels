# THIS IS THE MAIN FILE #
# This file will focus on updating the screen

# --- IMPORTS --- #
import pygame
import os # used to load image files in "image-files"


# --- SETUP VARIABLES --- #
# Game setup
gameGrid = [ # represents game grid
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
]

player1Cards = [0, 0, 0, 0]
player2Cards = [0, 0, 0, 0]

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


# --- HELPER FUNCTIONS --- #
def drawBasics():
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    # load in background
    screen.blit(background_image, (0, 0))

    # draw towers

    # draw Guys
    # ~ 108 x 108 pixel square

    pygame.display.flip()


# --- MAIN LOOP --- #
running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # user input turn
    player = 1
    while player > 0:

        drawBasics() # draw background, draw Guy positions
        if player == 1:
            # player 1 setup
            # blank right half of screen
            pygame.draw.rect(screen, "black", (windowWidth/2, 0, windowWidth/2, windowHeight))
            # pull up P1 cards
        
        if player == 2:
            # player 2 setup
            # blank left half of screen
            pygame.draw.rect(screen, "black", (0, 0, windowWidth/2, windowHeight))
            # pull up P2 cards

        # do stuff with cards


        # END OF TURN
        # if player == 1:
            # blank whole screen
            # prompt for P2

        # if player == 2:
            # exit while loop
            # player = -1

    # run game logic
    for row in gameGrid:
        for guy in row:
            guy.update()

    drawBasics()

    print("hello world")

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()