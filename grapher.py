import pygame
import math
from graph import Graph
from graph import Vertex
import helpers

pygame.init()

SCREEN_X = 500
SCREEN_Y = 500
ZOOM = 40
VERTEX_RADIUS = int(ZOOM / 7)
MIDDLE_Y = int((SCREEN_Y / ZOOM) / 2)
 
VERTEX_COLOR = (247, 72, 59)
BACKGROUND_COLOR = (255, 255, 255)
GRAPH_LINE_COLOR = (196, 196, 196)

size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grapher - SimpleSimple Graph Theory by Keith Yong")

done = False
clock = pygame.time.Clock()

g = Graph()
screen.fill(BACKGROUND_COLOR)
helpers.drawGraphLines(screen, SCREEN_X, SCREEN_Y, ZOOM, GRAPH_LINE_COLOR)
pygame.display.flip()

vertexCount = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(BACKGROUND_COLOR)
            # Add a new vertex to graph g with key = vertexCount
            g.addVertex(vertexCount)
            helpers.drawGraphLines(screen, SCREEN_X, SCREEN_Y, ZOOM, GRAPH_LINE_COLOR)
            # Draw a circle for the newly added vertex
            helpers.drawGraph(screen, g, ZOOM, VERTEX_COLOR, SCREEN_X, SCREEN_Y)
            vertexCount = vertexCount + 1
    pygame.display.flip()
    clock.tick(10)
