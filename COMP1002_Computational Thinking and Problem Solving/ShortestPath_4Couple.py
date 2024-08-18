from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        
def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

# Because the findShortestPath function isn't efficient, I use the Djikstra’s algorithm to find the shortest path
# The source: http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/



def solver():
    allStates = genStates()
    # generate all possible cases
    # state = XXXXXXXXXXX
    # 1st X = The position of boat(E/W)
    # 2nd and 3rd X = red husband and red wife
    # 4th and 5th X =  blue husband and blue wife
    #     ...     X =  green husband and green wife
    #     ...     X =  yellow husband adn yellow wife
    #     ...     X =  black husband and black wife'
    
    
    graph = genGraph(allStates) # generate a dictionary of path and change it to the object in class Graph() for using the Djikstra’s algorithm function
    path = dijsktra(graph, 'EEEEEEEEEEE', 'WWWWWWWWWWW')
    printPath(path) # print the shortest path that satisfies the requirement
    

    

def genStates():
    allStates = []
    states = ["EE","EW","WE","WW"]

    for i in ["E","W"]:
        for j in states:
            for k in states:
                for l in states:
                    for m in states:
                        for n in states:
                            allStates.append(i+j+k+l+m+n)
    return allStates

    
def genGraph(allStates):
    legalStates = []
    graph = {}
    edges=[]

    for i in allStates:
        if isLegal(i):
            legalStates.append(i)
    # append the legal node to the legalStates
    

    for i in legalStates:
        setNextNodes = nextStates(i,legalStates)
        graph.update({i:setNextNodes})
        
    # update the graph

    for i in graph:
        for j in graph[i]:
            if i != "WWWWWWWWWWW":
                tup = ( i , j ,1)
            edges.append(tup)

    graph2 = Graph()
    
    for edge in edges:
        graph2.add_edge(*edge)
        
    # change the dictionary to the graph object

    return graph2
#generate the Graph object and return it
    

def isLegal(S):
    if S[1] != S[2] and (S[2] == S[3] or S[2] == S[5] or S[2] == S[7] or S[2] == S[9] ):
        return False
    if S[3] != S[4] and (S[4] == S[1] or S[4] == S[5] or S[4] == S[7] or S[4] == S[9] ):
        return False
    if S[5] != S[6] and (S[6] == S[1] or S[6] == S[3] or S[6] == S[7] or S[6] == S[9] ):
        return False
    if S[7] != S[8] and (S[8] == S[1] or S[8] == S[3] or S[8] == S[5] or S[8] == S[9] ):
        return False
    if S[9] != S[10] and (S[10] == S[1] or S[10] == S[3] or S[10] == S[5] or S[10] == S[7] ):
        return False 
    if S[0] != S[1] and S[1] == S[2] == S[3] == S[4] == S[5] == S[6] == S[7] == S[8] ==S[9] ==S[10]:
        return False
    return True




def nextStates(aState,legalStates):

    neighborStates = []

    for i in legalStates:
        
        condition = True
        diff = 0
        
        if aState[0] != i[0]:
            for j in range(1,11):
                if aState[j] == aState[0] and aState[j] != i[j]:
                    diff += 1
                elif aState[j] != i[j]:
                    condition = False

        if diff > 0 and diff < 4 and condition:
            neighborStates.append(i)

    return neighborStates

#Find the linking states



def printPath(path):

    couples = ['red husband', 'red wife', 'blue husband', 'blue wife', 'green husband', 'green wife', 'yellow husband', 'yellow wife', 'black husband', 'black wife']
       
    for i in range(len(path)):
        the = str(i+1)+' The ' 
        who = []
        if path[i][0] == "E":
            direction ='from the east to the west'
        else:
            direction ='from the west to the east'
            
        if path[i] != 'WWWWWWWWWWW':
            for j in range(1,11):
                if path[i][j] != path[i+1][j]:
                    who.append(j-1)
            # find the person whose direction charge
            
            if len(who) == 1:
                print(the + couples[who[0]]+' goes '+ direction)
            elif len(who) == 2:
                print(the + couples[who[0]]+' and '+couples[who[1]]+' go '+ direction)
            else:
                print(the + couples[who[0]]+', '+couples[who[1]]+' and '+couples[who[2]]+' go '+ direction)
# print the shortest path            

solver()
