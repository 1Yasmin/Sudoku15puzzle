from funciones import *
from node import node
import copy

def AStart(problem):

    if(problem.protype == 1):
        frontier = []
        frontier = []
        explored = []
        path = [] #Result from A*
        
        state = problem.initial
        path.append(state)
        frontier.append(path)
        
    if(problem.protype == 2):
        #nodos cercanos
        frontier = problem.initial
        #estados prima guardados
        explored = []
        process = []
        
    
    
    while True:
        
        #print("-----FRONTIER----")
        #print(len(frontier))
        #for i in frontier:
         #   print(i.x , i.y)
        
        if len(frontier):

            if(problem.protype == 1):
                path = remove_choice1(problem, frontier)
                state = path[len(path)-1]
                explored.append(state)
                frontier.remove(path)
                #next state
                drawMatrix(state)
                
                #Test
                if problem.goal_test(state):
                    return path

                #Expansion
                probability = problem.actions(state)
                for i in probability:
                    if i not in explored: 
                        new_path = copy.deepcopy(path)
                        new_path.append(i)
                        frontier.append(new_path)

            if(problem.protype == 2):
                #devuelve el nodo que debe moverse
                path = remove_choice2(frontier, problem,problem.matrix, process)
                process.append(path)
                print("PROCESS")
                print(len(process))
                print("Path--------------------------------------")
                print(path.x , path.y)
                #estado de la matriz dado el path
                s = change(problem.matrix, blanknode(problem.matrix,4,0), process[-1])
                tempS = s.copy()
                explored.append(tempS)
                problem.matrix = s
                
                print (explored)

                if(problem.goalTest(s)):
                    return process

                frontier = []

                print("- Next State-")
                print(s)

               # print("explorados")
                #print(explored)

                for a in problem.actions(s):
                    temp = s.copy()
                    result = problem.result(temp,a)
                    #if result not in explored:
                    #d = revExplored(explored, result)
                    #print("RESPUESTA")
                    #print(d)
                    if (revExplored(explored, result) == False):
                        #print("Accion no explorada----------------------")
                        #print(a)
                        # nodo que se va a mover
                        new_path = newFrontier(s,a)
                        frontier.append(new_path)
        else:
            return print("El problema no tiene solucion")    



def remove_choice1(problem, frontier):
    pass

def remove_choice2(frontier, problem,s, process):

    posibles = []
    for i in frontier:
        posibles.append(PuzzleHeuristic(i, problem,s, process))
    
    return frontier[posibles.index(min(posibles))]
    
    

def PuzzleHeuristic(nod, problem,s, process):
    misplace = 0
    val = problem.pathCost(process) + misplace
    res = change(s, blanknode(s,4,0),nod)
   
    for x in range(4):
        for y in range (4):
            value1 = s[x,y]
            value2 = res[x,y]
            if value1 != value2:
                misplace = misplace+1
    return val
    



