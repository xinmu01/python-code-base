class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor (self, nbr, weight = 0): # nbr is a vertex object
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + "connected to " + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices += 1
        self.vertList[key] = Vertex(key)
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            print ("{} is not in graph".format(key))
            return None
    def __contains__(self,key): ## overload in
        return key in self.vertList
    def addEdge(self, f, t, weight = 0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g: ## This uses __iter__
        for w in v.getConnections(): 
            #print("(%s, %s)" % (v.getId(),w.getId()))
            print('({},{})'.format(v.getId(),w.getId()))
    if 0 in g: ## this uses __contains__
        print ('True')
    
        
