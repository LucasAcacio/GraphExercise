import res

####################################
############# INPUT OP #############
####################################

vertexList = []
edgeList = []
line = ""
val = ""
val2 = ""

option = input("Would you like to use a file as input?(y/n)")

if option == 'y':
	path = input("Insert file path: ")
	with open(path, 'r') as f: 
		data = f.read().splitlines()

	val = data[0]
	val2 = data[1]
	for x in data[2:]:
		node = x.split()
		edgeList.append(node)
  
	for x in edgeList:
		if x[0] == x[1]: edgeList.pop(x)
  
	for i in edgeList:
		for x in i:
			if x not in vertexList and x.isalpha() : vertexList.append(x)			

elif option == 'n':
	val = input("Choose if your graph will be directed or non-directed(d/n): ")
	val2 = input("Choose if your graph will your graph will be weighted or not weighted(w/n): ")

	if val2 == 'n':
		print("Please input graph stream: (please press $quit to finish the stream)\nExample graph: a b")

	if val2 == 'w':
		print("Please input graph stream: (please press $quit to finish the stream)\nExample graph: a b 3")

	while (line != "$quit"):
		line = input("Enter node: ")
		aux = []
  
		if (line == "$quit"):
			break
		else:
			node = line.split()
		for i in node: 
			aux.append(i)

		aux1 = aux[0]
		aux2 = aux[1]
  
		if aux1 not in vertexList: vertexList.append(aux1)
		if aux2 not in vertexList: vertexList.append(aux2)

		edgeList.append(aux)
		for x in edgeList:
			if x[0] == x[1]: edgeList.pop(edgeList.index(x))

##########################################
############### PROCESS OP ###############
##########################################

print("############## Incidence matrix graph representation ##############\n")
line = "   "
for x in vertexList:
    line = line + str(x) + "  "
print(line)

if val == 'n':  
	if val2 == 'n':
		matrix = res.getNonDirectedGraphMatrix(vertexList, edgeList)

		count = 0
		for a in matrix:
			print(f"{vertexList[count]} {a}")
			count+=1

	elif val2 == 'w':
		matrix = res.getNonDirectedWeightedGraph(vertexList, edgeList)

		count = 0
		for a in matrix:
			print(f"{vertexList[count]} {a}")
			count+=1

	else:
		print("Invalid model, ending program. . .")

elif val == 'd':
	if val2 == 'n':
		matrix = res.getDirectedGraphMatrix(vertexList, edgeList)
		count = 0
		for a in matrix:
			print(f"{vertexList[count]} {a}")
			count+=1

	elif val2 == 'w':
		matrix = res.getDirectedWeightedGraph(vertexList, edgeList)

		count = 0
		for a in matrix:
			print(f"{vertexList[count]} {a}")
			count+=1

	else:
		print("Invalid model, ending program. . .")

else:
 	 print("Invalid model, ending program. . .")
  
print("\n############## GRAPH INFO ##############\n")
print(f"| Graph order: {len(edgeList)}")
print(f"| Graph size: {len(vertexList)}")

######################################
###############POST OPS###############
######################################
postOps = ""
while postOps != "4":	
	postOps = input("\n############## Post operations list ##############\n| 1 - Check vertex adjacency list\n| 2 - Check vertex degree\n| 3 - Check if 2 vertex are adjacent\n| 4 - Quit\n >>>")
	
	if postOps == "1":
		vertex = input("\n|Insert vertex name: ")
		if vertex in vertexList:
			if val == "n":
				adjList = res.getNonDirectedAdjacencyList(vertex, edgeList)
				print(f"Vertex <{vertex}> adjacency list: {adjList}")
			else:
				entranceList = res.getEntranceAdjacencyList(vertex, edgeList)
				exitList = res.getExitAdjacencyList(vertex, edgeList)
				
				if len(entranceList) > 0: print(f"Vertex <{vertex}> <--- {entranceList}")
				if len(exitList) > 0: print(f"Vertex <{vertex}> ---> {exitList}")
			
		else:
			print("Vertex not present!")

	elif postOps == "2":
		vertex = input("\n|Insert vertex name: ")
		if vertex in vertexList:
			if val == "n":
				adjList = res.getNonDirectedAdjacencyList(vertex, edgeList)
    
				print(f"Vertex <{vertex}> degree: {len(adjList)}")
    
			else:
				entranceList = res.getEntranceAdjacencyList(vertex, edgeList)
				exitList = res.getExitAdjacencyList(vertex, edgeList)
    
				print(f"Vertex <{vertex}> entrance Degree: {len(entranceList)}")
				print(f"Vertex <{vertex}> exit Degree: {len(exitList)}")
    
		else:
			print("Vertex not present!")
   
	elif postOps == "3":
			vertex1 = input("\n|Insert first vertex name: ")
			vertex2 = input("|Insert second vertex name: ")
			if vertex1 and vertex2 in vertexList:
				if val == "n":
					adjList1 = res.getNonDirectedAdjacencyList(vertex1, edgeList)
		
					if vertex2 in adjList1: print(f"\nVertex <{vertex1}> and <{vertex2}> are adjacent>")
					else: print(f"\nVertex <{vertex1}> and <{vertex2}> are not adjacent")
		
				else:
					adjList1 = res.getDirectedAdjacencyList(vertex1, edgeList)
					if vertex2 in adjList1: print(f"\nVertex <{vertex1}> is adjacent to <{vertex2}>")
					else: print(f"\nVertex <{vertex1}> is not adjacent to <{vertex2}>")
	
			else:
				print("\nInvalid pair of vertex")



