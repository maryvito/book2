class MyVertex:
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


class MyGraph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = MyVertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, t,f, cost = 0):
        if t not in self.vertList:
            nv = self.addVertex(t)
        if f not in self.vertList:
            nv = self.addVertex(f)
        self.vertList[t].addNeighbor(self.vertList[f], cost)


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())




g = MyGraph()
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for n in v.getConnections():
        print("(%s , % s)" % (str(v.getId()), str(n.getId())))

