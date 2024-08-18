shortestLegalStates = set()

def solver():
    setAllStates = genAllStates()
    setAllLegalStates = genSectionA(setAllStates)
    G = genGraph(setAllLegalStates)
    shortest_path = findShortestPath(G, "EEEEEEEEE", "WWWWWWWWW", path=[])
    genSectionB(G,setAllLegalStates)
    genSectionC(shortest_path)






def genAllStates():
    """
    This function generates a set of all possible states (E/W)*9.
    Input: None
    Output: Return a set of all possible states (E/W)*9
    """

    side = ["E","W"]
    states = ["".join((Bo,Mo,Ph,Ah,Je,AhSer,An,Sa,AnSer)) for Bo in side for Mo in side for Ph in side \
                                                          for Ah in side for Je in side for AhSer in side\
                                                          for An in side for Sa in side for AnSer in side]
    return tuple(states)



def StateCondition(state):
    """
    This function determines the condition of a state (legal/illegal). When it is illegal, the constraint that violated will also be determined.
    Input: A state
    Output: If a state is legal, return a list with 4 False elements; else, return a list with 1/2/3 True elements (i.e. representing the constraint(s) it violated)
    """

    constraint = [False]*4
    # The if() statement expresses the condition of illegal state that violate each constraint
    if (state[0] != state[1] and state[1] == state[2] == state[3] == state[6]):                                          #violates C1
        constraint[0] = True
    if (state[1] != state[2] and not state[1] == state[3] == state[4] == state[5] == state[6] == state[7] == state[8]):  #violates C2
        constraint[1] = True
    if (state[3] != state[4] and state[4] == state[6]) or (state[3] != state[5] and state[5] == state[6]):               #violates C3
        constraint[2] = True
    if (state[6] != state[7] and state[7] == state[3]) or (state[6] != state[8] and state[8] == state[3]):               #violates C4
        constraint[3] = True
    return constraint



def genSectionA(S):
    """
    This function return a list with all legal states and generates the printing of section A by separating states in different conditions
    Input: A set of all possible states
    Output: Return a list with all legal states and printing based on a set of all possible states and given constraints
    """
    #Create empty lists to store states with each condition
    
    legal = []    #legal states
    c1 = []       #states that violates C1
    c2 = []       #states that violates C2
    c3 = []       #states that violates C3
    c4 = []       #states that violates C4
    c2c3 = []     #states that violates C2 and C3
    c2c4 = []     #states that violates C2 and C4
    c3c4 = []     #states that violates C3 and C4
    c2c3c4 = []   #states that violates C2, C3 and C4
    onlyc2 = []   #states that violates only C2
    onlyc3 = []   #states that violates only C3
    onlyc4 = []   #states that violates only C4


    #append states into lists with determining which constraint(s) is/are violated
    #e.g. constraint list  =  [False]*4  ==  legal state
    #e.g. constaint list  =  [False,True,True,True]  == state that violates C2,C3,C4

    for i in range(len(S)):
        con = StateCondition(S[i])    #get the constraint list of the state by calling StateCondition function

        if con == [False]*4:
            legal.append(S[i])
        if con[0] == True:
            c1.append(S[i])
        if con[1] == True:
            c2.append(S[i])
            if con[2] == True:
               c2c3.append(S[i])
            if con[3] == True:
               c2c4.append(S[i])
            if con[2] == True and con[3] == True:
                c2c3c4.append(S[i])
        if con[2] == True:
            c3.append(S[i])
            if con[3] == True:
               c3c4.append(S[i])
        if con[3] == True:
            c4.append(S[i])


    print("SECTION A: THE STATE SPACE\n")
    print(f"The set of legal states: ({len(legal)})")
    for i in range(len(legal)):
        if i%6 == 0 and i!=0:
            print()  
        print(legal[i],end=" ")
    print("\n")


    print(f"(C1): The set of illegal states that violates the constraint of having the boat with at least a man: ({len(c1)})")
    for i in range(len(c1)):
        if i%6 == 0 and i!=0:
            print()  
        print(c1[i],end=" ")
    print("\n")


    print(f"(C2): The set of illegal states that violates the constraint of preventing Pharaoh from beating others: ({len(c2)})")
    for i in range(len(c2)):
        if i%6 == 0 and i!=0:
            print()  
        print(c2[i],end=" ")
    print("\n")


    print(f"(C3): The set of illegal states that violates the constraint of preventing Ananias from beating Ahab's household: ({len(c3)})")
    for i in range(len(c3)):
        if i%6 == 0 and i!=0:
            print()  
        print(c3[i],end=" ")
    print("\n")


    print(f"(C4): The set of illegal states that violates the constraint of preventing Ahab from beating Ananias's household: ({len(c4)})")
    for i in range(len(c4)):
        if i%6 == 0 and i!=0:
            print()  
        print(c4[i],end=" ")
    print("\n")


    print(f"The set of illegal states that violates both C2 and C3: ({len(c2c3)})")
    for i in range(len(c2c3)):
        if i%6 == 0 and i!=0:
            print()  
        print(c2c3[i],end=" ")
    print("\n")


    print(f"The set of illegal states that violates both C2 and C4: ({len(c2c4)})")
    for i in range(len(c2c4)):
        if i%6 == 0 and i!=0:
            print()  
        print(c2c4[i],end=" ")
    print("\n")


    print(f"The set of illegal states that violates both C3 and C4: ({len(c3c4)})")
    for i in range(len(c3c4)):
        if i%6 == 0 and i!=0:
            print()  
        print(c3c4[i],end=" ")
    print("\n")


    print(f"The set of illegal states that violates both C2, C3 and C4: ({len(c2c3c4)})")
    for i in range(len(c2c3c4)):
        if i%6 == 0 and i!=0:
            print()  
        print(c2c3c4[i],end=" ")
    print("\n")


    for state in c2:                                                                  
        if (state not in c2c3) and (state not in c2c4) and (state not in c2c3c4):     #if a state only violates only C2, it should not be inside any lists of states that violated C2C3, C2C4, and C2C3C4
            onlyc2.append(state)
    print(f"The set of illegal states that violates only c2: ({len(onlyc2)})")
    for i in range(len(onlyc2)):
        if i%6 == 0 and i!=0:
            print()
        print(onlyc2[i],end=" ")
    print("\n")


    for state in c3:
        if (state not in c2c3) and (state not in c3c4) and (state not in c2c3c4):     #similar to the case above
            onlyc3.append(state)
    print(f"The set of illegal states that violates only c3: ({len(onlyc3)})")
    for i in range(len(onlyc3)):
        if i%6 == 0 and i!=0:
            print()
        print(onlyc3[i],end=" ")
    print("\n")


    for state in c4:
        if (state not in c2c4) and (state not in c3c4) and (state not in c2c3c4):     #similar to the case above
            onlyc4.append(state)
    print(f"The set of illegal states that violates only c4: ({len(onlyc4)})")
    for i in range(len(onlyc4)):
        if i%6 == 0 and i!=0:
            print()
        print(onlyc4[i],end=" ")
    print("\n")


    return legal    #return a list of legal states for doing Section B






def genGraph(L):
    """
    This function generates a graph to show relationship between nodes
    (i.e. keys = each node, values = a list of neighboring states of each node)
    Input: A list of all legal states
    Output: Return a graph (dictionary) based on a list of all legal states
    """
    graph = {}
    for i in range(len(L)):
        setNextNodes = nextStates(L[i],L)
        graph.update({L[i]:setNextNodes})
        
    return graph



def findShortestPath(graph, start, end, path=[]):
    """
    This function finds a shortest path from "start" to "end" on a graph
    This function is obtained from https://www.python.org/doc/essays/graphs/
    with one change due to the deprecation of the method has_key().
    
    Input: A graph ('graph'), a starting node ('start'), an end node ('end') and an empty path ('path')
    Output: Returns a shortest path from 'start' and 'end'.    
    """
    # source: A7
    
    global shortestLegalStates
    
    path = path + [start]
    if start == end:           # when current node reaches the end, return the path
        return path
    if not (start in graph):   #if the starting node is not a state in graph, we cannot find the solution
        return None
    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):    # compare the current shortest path with the new path
                    shortestPath = newpath
                    for i in shortestPath:          # put all the legal states that are part of at least one shortest path into a set for Section B
                        shortestLegalStates.add(i)  

    return shortestPath    



def nextStates(aState,allStates):
    """
    This function returns a set of states that a given state can go to.
    Input: A state(aState) and a set of all states
    Output: A set of states from allStates that aState can go to (i.e. neighboring states)
    """
    # source: A7
    
    neighborStates = []
    
    for i in allStates:
        if neighborNode(aState,i) == True:
            neighborStates.append(i)
            
    return neighborStates


    
def neighborNode(state1,state2):
    """
    This function determines whether state1 and state 2 are neighboring states
    (i.e. the boats are on different sides and there are no more than 2 changes in
    their positions)
    Input: Two states (state1, state2)
    Output: Return True if they are neighboring states; else, False
    """
    diff = 0                               #count the total number of changes between 2 states
    if state1[0] != state2[0]:             #when the position of boat is moved,
        for i in range(1,9):
            if state1[i] == state1[0]:     #if any character moves with the boat (i.e. changed its position)
               if state1[i] != state2[i]:  #add 1 to the total number of changes
                  diff += 1
            else:
                if state1[i] != state2[i]: #character can never move without the boat
                    return False
    else:
        return False        #neighboring states must consist of the change of the boat's position
    
    men = [1,2,3,6]              #1,2,3,6 indicate the indexes of Moses,Pharaoh,Ahab and Ananias's positions
    only_men_operate = False
    if state1[0] != state2[0]:
        for i in range(1,9):
            if state1[i] == state1[0]:                       # if one of the characters moves with the boat
                if state1[i] != state2[i] and i in men:      # and he is a man (Moses/Pharaoh/Ahab/Ananias),
                   only_men_operate = True                   # state 2 can be a neighboring state of state 1  (i.e. not violating C1)


    if diff>0 and diff<3 and only_men_operate == True:   #neighboring states must have no more than 2 changes in the positions & they must not violate C1
        return True
    else:
        return False


   
def genSectionB(graph,L):
    """
    This function generates the printing of Section B.
    Input: A graph of all legal states and a list of all legal states
    Output: A print out of the graph related to shortest path's nodes and links
    """
    
    print("SECTION B: FORMING A GRAPH\n")

    print("There are",len(shortestLegalStates),"legal states that are part of at least one shortest path.")
    for i in sorted(shortestLegalStates):    # sort the nodes in the shortest path
        states = []
        for j in shortestLegalStates:   # loop the states in the list stroing all the legal states that are part of at least one shortest path
            if j in graph[i]:           # if the state is inside the value of the graph with key of "i",
                states.append(j)        # append it into a new list as to print out the graph in Section B
                states.sort()
        print(i,states)

    print("\nThere are",(len(L)-len(shortestLegalStates)),"legal states that are NOT part of any shortest path.")
    NOT = []
    for i in graph:                         # loop the keys in the graph storing all legal states
        if i not in shortestLegalStates:    # if a state is not part of at least one shortest path,
            NOT.append(i)                   # append it into a list storing legal states that are NOT part of any shortest path
    for i in range(len(NOT)):
        if i%6 == 0 and i!=0:
            print()
        print(NOT[i],end=" ")               # print out all the legal states that are NOT part of any shortest path with format
    print("\n")






def genSectionC(path):
    """
    This function generates the printing of Section C. 
    Input: A list of nodes that represents shortest path
    Output: A print out of the status of the characters (i.e. who is/are on the east and who is/are on the west) and the steps of moving
    """
  
    characters = ["","Moses","Pharaoh","Ahab","Jezebel","servant of Ahab","Ananias","Sapphira","servant of Ananias"]

    print("\nSECTION C: SHORTEST PATHS\n")

    for node in range(len(path)-1):
        
        if path[node][0] == "E":           #if the boat is on the East, then the moving direction should be from the east to the west
            fromDirection = "east"
            toDirection = "west"       
        else:
            fromDirection = "west"         #if the boat is on the West, then the moving direction should be from the west to the east
            toDirection = "east"


        east = []                             # create lists to store the characters that are on the east and on the west respectively
        west = []
        for i in range(1,len(path[node])):
            if path[node][i] == "E":
                east.append(characters[i])  
                east.sort()
            else:
                west.append(characters[i])
                west.sort()

        print("East:",east)                   # print the status in each iteration and the lists will be blank again in the next iteration
        print("West:",west)

        
        whichChracterCrossing = ""
        for i in range(1,len(path[node])):
            if path[node][i] != path[node+1][i]:                             # if a character moves,
                whichChracterCrossing = whichChracterCrossing + str(i)       # store its index in "whichChracterCrossing"

                
        printLine = ""
        if len(whichChracterCrossing) == 1:                                                   # if there is only 1 index, that means only 1 character moves
            printLine = printLine + characters[int(whichChracterCrossing[0])] + " goes "      # else, there are 2 characters move.
        else:
            printLine = printLine + characters[int(whichChracterCrossing[0])] + " and " + characters[int(whichChracterCrossing[1])] + " go "

        printLine = printLine + "from the " + fromDirection + " to the " + toDirection + "."   # combine the sentence with the moving direction

        
        print("("+ str(node+1) +")",printLine,"\n")



solver()
