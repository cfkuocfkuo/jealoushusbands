'''
Created on 29.10.2014

@author: Lorenzo Ritter
'''
from copy import deepcopy
import time
import sys

class Shore:
    state = None
    boat = 0
    depth = 0                           # equals path cost in this example because unit step cost = 1
    path = None
    
    def __init__(self, s=[], b=0):
        self.state = s
        self.boat = b
        self.depth = 0
        self.path = []
        
    def f(self):                        # evaluation function
        return self.depth + h(self)
          

def jealousy(current):
    for i in range(0,noCouples):
        if current.state[i] != current.state[noCouples+i]:          # husband is not with his wife
            for j in range(noCouples, noCouples*2): 
                    if(current.state[j] == current.state[i]):       # another husband is with the wife, so jealousy occurs
                        return 1
    return 0

def alterbit(bit):
    return abs(bit - 1)

def isGood(shore):                                                  # people on the same side as the boat are "good"
    good_people = deepcopy(initial.state)
    for i in range(0, len(shore.state)):
        if shore.state[i] == shore.boat:
            good_people[i] = 1
    return good_people

def h(shore):
    result = len(shore.state)
    for i in shore.state:
        result = result - i
    return result

def visited(shore, searched):
    for k in range(0, len(searched)):
        if shore.state == searched[k].state and shore.boat == searched[k].boat:
            return True
    return False

def expand(shore):
    good_people = isGood(shore)                                     # people on the same side as the boat are "good"
        
    for i in range(0, len(shore.state)):                            # iterate through all possible state changes
        for j in range(i, len(shore.state)):
            following = deepcopy(shore)
            if(good_people[i]==1 and good_people[j]==1):            # check that the persons are on the same side as the boat
                following.state[i]=alterbit(following.state[i])     # move first person
                if(i != j):                                         # move second person if different from first person
                    following.state[j]=alterbit(following.state[j])
                following.boat = alterbit(following.boat)           # move boat
                if visited(following, searched):                    # check if state was already visited
                    True
                elif jealousy(following):                           # check if there is jealousy
                    searched.append(following)
                elif True:
                    following.depth = following.depth + 1           # increase depth
                    following.path.append(shore)                    # add the parent node to the path
                    frontier.append(following)                         # add the node to the frontier
            else:
                True


def BFS(inode):
    d = -1                                      # current depth
    noStates = 0
    while True:
        noStates = noStates + 1
        
        current = frontier.pop(0)                               # examine first item from frontier (FIFO)
        
        current.heur = h(current)
        if current.heur == 0:                                   # goal check
            print("\nVisited states: ", noStates)               # if heuristic function equals 0, the goal is reached
            return current
        
        if current.depth != d:                                  # print depth if changed
            d = current.depth
            print("current depth: ", d, "\tcalculating...")
        
        expand(current)                                         # expand and add new states to frontier
        searched.append(current)                                # add the current node to the closed list

def DFS(inode):
    noStates = 0
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        current = frontier.pop()                                # examine last item from frontier (LIFO)
        
        current.heur = h(current)
        if current.heur == 0:                                   # goal check
            return current                                      # if heuristic function equals 0, the goal is reached
        
        expand(current)                                         # expand and add new states to frontier
        searched.append(current)                                # add the current node to the closed list

def GBEST(inode):
    noStates = 0
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        frontier.sort(key=lambda Shore: h(Shore))               # sort frontier according to heristic function
        
        current = frontier.pop(0)                               # examine first item of the frontier (item with the lowest heuristic function)
        
        current.heur = h(current)
        if current.heur == 0:                                   # goal check
            return current                                      # if heuristic function equals 0, the goal is reached
        
        expand(current)                                         # expand and add new states to frontier
        searched.append(current)                                # add the current node to the closed list
        
def ASTAR(inode):
    noStates = 0
    while True:
        noStates = noStates + 1
        print("Visited states: ", noStates)
        
        frontier.sort(key=lambda Shore: Shore.f())              # sort frontier according to exaluation function
        
        current = frontier.pop(0)                               # examine first item of the frontier (item with the lowest evaluation function)
        
        current.heur = h(current)
        if current.heur == 0:                                   # goal check
            return current                                      # if heuristic function equals 0, the goal is reached
        
        expand(current)                                         # expand and add new states to frontier
        searched.append(current)                                # add the current node to the closed list
                
if __name__ =='__main__':
    noCouples = int(input("Enter the number of couples: "))
    
    time.perf_counter()
    
    couple = [0,0]
    initial = Shore([], 0)
    goal = Shore([], 0)
    path = []
    
    for i in range(0,noCouples):                        # add couples on left side of the river
        initial.state.extend(couple)                    # the state will be treated as wife1, wife2, wife3, ... husband1, husband2, husband3, ...
    
    frontier = []                                      # open list (frontier)
    searched = []                                       # closed list
    
    frontier.append(initial)                           # add initial node to frontier
    
    print("\nsearch strategies:")
    print("\t(1) Breadth-First-Search")
    print("\t(2) Depth-First-Search")
    print("\t(3) Greedy Best-First-Search")
    print("\t(4) A*-Search-Algorithm")
    selection = int(input("Select the search strategy you would like to use: "))
    
    if(selection==1):
        goal = BFS(initial)                             # search with Breadth-First-Search
    elif(selection==2):
        goal = DFS(initial)                             # search with Depth-First-Search
    elif(selection==3):
        goal = GBEST(initial)                           # search with Greedy Best-First-Search
    elif(selection==4):
        goal = ASTAR(initial)                           # search with A*-Search-Algorithm
    else:
        print("invalid selection")
        sys.exit()
    
    print("\nSuccess: ", goal.state, " reached")
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.state)
    print("Path: ", path)
    print("elapsed time: %.2fs" % time.perf_counter())
