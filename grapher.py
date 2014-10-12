import pygame
import math
from graph import Graph
from graph import Vertex
import helpers

pygame.init()

SCREEN_X = 500
SCREEN_Y = 500
ZOOM = 100
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

g = Graph()
screen.fill(WHITE)
helpers.drawGraphLines(screen, SCREEN_X, SCREEN_Y, ZOOM, graph_line_color)
pygame.display.flip()

vertexCount = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add a new vertex to graph g with key = vertexCount
            g.addVertex(vertexCount)

            # Draw a circle for the newly added vertex
            helpers.drawGraph(screen, g, ZOOM, RED)
            vertexCount = vertexCount + 1
    pygame.display.flip()
    clock.tick(10)
