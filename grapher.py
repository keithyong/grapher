import pygame
import math
import graph
import helpers

pygame.init()

SCREEN_X = 500
SCREEN_Y = 500
ZOOM = 20
VERTEX_RADIUS = int(ZOOM / 7)
MIDDLE_Y = int((SCREEN_Y / ZOOM) / 2)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

graph_line_color = (201, 203, 207)

size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grapher - SimpleSimple Graph Theory by Keith Yong")

done = False
clock = pygame.time.Clock()

g = graph.Graph()
screen.fill(WHITE)
helpers.drawGraphLines(screen, SCREEN_X, SCREEN_Y, ZOOM, graph_line_color)
pygame.display.flip()

while not done:
    pygame.display.flip()
    clock.tick(10)
