import pygame
import sys
scr = pygame.display.set_mode((400,440))
while 1:
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             sys.exit()
    pygame.display.flip()
