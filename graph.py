import pygame
import math

pygame.init()

SCREEN_X = 500
SCREEN_Y = 500
ZOOM = 20
VERTEX_RADIUS = int(ZOOM / 7)
MIDDLE_Y = int((SCREEN_Y / ZOOM) / 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

graph_line_color = (100, 100, 100)

size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grapher - Simple Graph Theory by Keith Yong")

done = False
clock = pygame.time.Clock()

def drange(start, stop, step):
    while start < stop:
        yield start
        start += step

screen.fill(WHITE)
for i in  drange(0, SCREEN_X, ZOOM):
    pygame.draw.aaline(screen, graph_line_color, [i, 0], [i, SCREEN_Y], True)

for i in drange(0, SCREEN_Y, ZOOM):
    pygame.draw.aaline(screen, graph_line_color, [0, i], [SCREEN_X, i], True)

pygame.display.flip()

vertex_x = 0
vertex_y = 0
while not done:
    lastVertex_x = vertex_x
    lastVertex_y = vertex_y
    vertex_x = ZOOM * int(input("What is x: "))
    vertex_y = ZOOM * int(input("What is y: ")) + (MIDDLE_Y * ZOOM)
    pygame.draw.circle(screen, RED, (vertex_x, vertex_y), VERTEX_RADIUS)
    pygame.draw.aaline(screen, BLACK, [lastVertex_x, lastVertex_y], [vertex_x, vertex_y], True)
    pygame.display.flip()
    clock.tick(10)

