# Helper functions for grapher app, to declutter the main program
import pygame
import graph
import math


def drange(start, stop, step):
    while start < stop:
        yield start
        start += step
        
def drawGraphLines(scr, scrX, scrY, zoom, color, width = 1):
    for i in  drange(0, scrX, zoom):
        pygame.draw.aaline(scr, color, [i, 0], [i, scrY], True)

    for i in drange(0, scrY, zoom):
        pygame.draw.aaline(scr, color, [0, i], [scrX, i], True)

# http://stackoverflow.com/a/7198179/529956
# [sides]-sided polygon with radius [radius]
# centered at [center]
# [n] = the desired vertex of that polygon
# NOTE: For different center simply add the coord
# to the returned x and y.
# 
# Returns the cartesian coordinate of 
# nth vertex of such polygon, in
# (int(x), int(y)) tuple format
def getPolygonVertexCoord(radius, n, sides, center):
    xCoord = radius * math.cos(2 * math.pi * n/sides)
    yCoord = radius * math.sin(2 * math.pi * n/sides)
    xCoord = int(xCoord + center[0])
    yCoord = int(yCoord + center[1])
    return (xCoord, yCoord)

def drawGraph(scr, gr, zoom, color, scrX, scrY):
    radius = int(zoom / 10)
    count = 0
    centerCoord = (scrX / 2, scrY / 2)
    radiusOfPolygon = scrX / 2.5
    vertexCoordDict = {}    # Planning on using this for edge coordinates

    for key in gr.getVertices():
        coord = getPolygonVertexCoord(radiusOfPolygon, count, gr.getNumVertices(), centerCoord)
        pygame.draw.circle(scr, color, (coord), radius)
        count = count + 1