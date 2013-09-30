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
to make the program stop.
