""" Demo presents a very minimal introductory program, using pygame to:
    1. Create and display an object on the screen
    2. Read in a music file, and loop continuous
    3. Read in a sound file, and play it in response to a game event

    This will be expanded to include reading in a graphic file,
    sprite movement, some window methods and others.
"""

import pygame
import sys
pygame.init()
FS = 22050
pygame.mixer.init(FS, -16, 2)
SCREEN = pygame.display.set_mode((400, 440))
RED = (255, 0, 0) # R,G,B, red green blue. The minimum number is 0,
                  # max is 255
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREEN.fill(RED)
SQUARE = pygame.Surface((25, 25)) # everything you want to
                                  # display is a Surface.
                                  # You tell it width, and height
SQUARE.fill(BLUE) # This says to fill the surface with the color Bblue
BACKGROUND_MUSIC = pygame.mixer.music.load('bu-bird-of-an-age.ogg')

LOOP_FOREVER = -1
pygame.mixer.music.play(LOOP_FOREVER)
EXPLODE = pygame.mixer.Sound('cfxrExplosion.wav')
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            else:
                EXPLODE.play()
    SCREEN.blit(SQUARE, (200, 210)) # blit writes a surface on another
                                 # surface. The two numbers say where:
                                 # x and y.
    pygame.display.flip()
