# Import Packages
import pygame as pg
from pygame.locals import *
from functions import *
from parameters import *

# Initiate Pygame
pg.init()

# Sets the screen width and height using the parameters in the parameters file
screen = pg.display.set_mode((WIDTH,HEIGHT))

# Set the name of the game on the display wondow
pg.display.set_caption("Connect Four")

# Colour the background of the game 
screen.fill(BACKGROUND)

# Set up the game loop
run = True
while run:
    # add event handlers
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
pg.display.update()

pg.quit()
