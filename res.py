def getNonDirectedGraphMatrix(vertexList, edgeList):
    matrix = []

    for x in vertexList:
      aux = []
      for y in vertexList:
          flag = 0
          for t in edgeList:
            if (x == t[0] and y == t[1]) or (x == t[1] and y==t[0]):
              flag = 1
          aux.append(flag)
    
      matrix.append(aux)

    return matrix

def getNonDirectedWeightedGraph(vertexList, edgeList):
    matrix = []

    for x in vertexList:
      aux = []
      for y in vertexList:
        value = 0
        for t in edgeList:
          if (x == t[0] and y == t[1]) or (x == t[1] and y == t[0]):
            value = int(t[2])
        aux.append(value)

      matrix.append(aux)

    return matrix

def getDirectedGraphMatrix(vertexList, edgeList):
    matrix = []

    for x in vertexList:
      aux = []
      for y in vertexList:
        flag = 0
        for t in edgeList:
          if (x == t[0] and y == t[1]):
            flag = 1
        aux.append(flag)

      matrix.append(aux)
    return matrix

def getDirectedWeightedGraph(vertexList, edgeList):
    matrix = []
    
    for x in vertexList:
      aux = []
      for y in vertexList:
        value = 0
        for t in edgeList:
          if (x == t[0] and y == t[1]):
            value = int(t[2])
        aux.append(value)

      matrix.append(aux)
    return matrix

def getNonDirectedAdjacencyList(vertex, edgeList):
    adjList = []
    for x in edgeList:
        if vertex == x[0]: adjList.append(x[1])
        elif vertex == x[1]: adjList.append(x[0]) 
    
    return set(adjList)
        
def getExitAdjacencyList(vertex, edgeList):
    adjList = []
    for x in edgeList:
        if vertex == x[0]: adjList.append(x[1])
    
    return adjList

def getEntranceAdjacencyList(vertex, edgeList):
  adjList = []
  for x in edgeList:
    if vertex == x[1]: adjList.append(x[0])
  
  return adjList

    
      