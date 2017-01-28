from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while(vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == "white"):
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)

        currentVert.setColor("black")







def traverse(y):
    x=y
    while(x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


g = Graph()
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

bfs(g, g.getVertex(0))
traverse(g.getVertex(4))

