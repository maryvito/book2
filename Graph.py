class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)+ ' connected to ' + str([x.id for x in self.connectedTo])

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
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def __contains__(self, item):
        return item in self.vertList

    def addEgge(self, t,f, cost = 0):
        if t not in self.vertList:
            nv = self.addVertex
        if f not in self.vertList:
            nv = self.addVertex(f)
        self.vertList[t].addNeighbor(self.vertList[f], cost)


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())



g = Graph()
g.addVertex("grandfather1")
g.addVertex("grandmather1")
g.addEgge("grandfather1", "grandmather1", 0)
g.addEgge("grandfasther2", "grandmather2", 0)
g.addEgge("grandfather1", "father1", 0)
g.addEgge("grandfather2", "father2", 0)

for v in g:
    for n in v:
        print("(%d , % d)") & (v.id, n.id)

