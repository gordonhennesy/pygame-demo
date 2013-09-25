import pygame
import sys
scr = pygame.display.set_mode((400,440))
red = (255,0,0) # R,G,B, red green blue. The minimum number is 0, max is 255
green = (0,255,0)
blue = (0,0,255)
scr.fill(red)
square = pygame.Surface((25,25)) # everything you want to display is a Surface. You tell it width, and height
square.fill(blue) # This says to fill the surface with the color blue
while 1:
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             sys.exit()
    pygame.display.flip()
