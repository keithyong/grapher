#http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html
#http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html
class Vertex:
    # Initialize a vertex that has
    # a dictionary 'connectedTo'
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    # Adds a neighbor vertex 'nbr' to this vertex
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    # Returns a string representation of vertex
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # Returns all vertices in the adjacency list
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]



class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    # Adds an edge between two vertices f and t. If f and/or t is not in
    # self.vertList
    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    # Get all vertices in this graph object's vertList
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
