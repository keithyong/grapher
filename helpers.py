import pygame

def drange(start, stop, step):
    while start < stop:
        yield start
        start += step
        
def drawGraphLines(scr, scrX, scrY, zoom, color, width = 1):
    for i in  drange(0, scrX, zoom):
        pygame.draw.aaline(scr, color, [i, 0], [i, scrY], True)

    for i in drange(0, scrY, zoom):
        pygame.draw.aaline(scr, color, [0, i], [scrX, i], True)
