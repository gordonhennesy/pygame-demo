pygame-demo
===========

I try to show you as much pygame as you need to start programming a game.

The simplest pygame program:

    import pygame

    scr = pygame.display.set_mode((400,440))
    while 1:
        pygame.display.flip()
        
Hmm, too simple. You need to Control-C (or whatever) to get out of the program.

Let's just add a few things to make it easier to get out of the program.

    import pygame
    import sys

    scr = pygame.display.set_mode((400,440))
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        
There, that's better. Now we can click on the go-away box in the upper corner
to make the program stop. I like to make it even easier, so I'll add the 
ESC (escape) key in the next example. Also colors

    import pygame
    import sys
    
    red = (255,0,0) # R,G,B, red green blue. The minimum number is 0, max is 255

    scr = pygame.display.set_mode((400,440))
    scr.fill(red)
    green = (0,255,0)
    blue = (0,0,255)
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:                  
                if event.key==pygame.K_ESCAPE:
                    sys.exit()
        pygame.display.flip()
