import pygame
import sys
pygame.init()
Fs=22050
pygame.mixer.init(Fs, -16, 2)
scr = pygame.display.set_mode((400,440))
red = (255,0,0) # R,G,B, red green blue. The minimum number is 0, max is 255
green = (0,255,0)
blue = (0,0,255)
scr.fill(red)
square = pygame.Surface((25,25)) # everything you want to display is a Surface. You tell it width, and height
square.fill(blue) # This says to fill the surface with the color blue
background_music = pygame.mixer.music.load('bu-bird-of-an-age.ogg')

loop_forever = -1
pygame.mixer.music.play(loop_forever)
explode = pygame.mixer.Sound('cfxrExplosion.wav')
while 1:
    
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             sys.exit()
         elif event.type==pygame.KEYDOWN:                  
             if event.key==pygame.K_ESCAPE:
                 sys.exit()
             else:
                 explode.play()
    scr.blit(square, (200,210)) # blit writes a surface on another surface. The two numbers say where: x and y.
    pygame.display.flip()
