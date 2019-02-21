from funciones import *
from node import node

def AStart(problem):
    #nodos cercanos
    frontier = problem.initial
    #estados prima guardados
    explored = []
    process = []
    
    while True: 
        print("-----FRONTIER----")
        #print(len(frontier))
        for i in frontier:
            print(i.x , i.y)
        
        if len(frontier):           
            #devuelve el nodo que debe moverse
            path = remove_choice(frontier, problem,problem.matrix, process)
            process.append(path)
            print("PROCESS")
            print(len(process))
            print("Path--------------------------------------")
            print(path.x , path.y)
            #estado de la matriz dado el path
            s = change(problem.matrix, blanknode(problem.matrix,4,0), process[-1])
            explored.append(s)
            problem.matrix = s
            
            #print (explored)

            if(problem.goalTest(s)):
                return process

            frontier = []

            print("- Next State-")
            print(s)

            print("explorados")
            print(explored)
            
            for a in problem.actions(s):
                temp = s.copy()
                result = problem.result(temp,a)
                if (revExplored(explored, result)):
                    #print("Accion no explorada----------------------")
                    #print(a)
                    # nodo que se va a mover
                    new_path = newFrontier(s,a)
                    frontier.append(new_path)
        else:
            return False    



def remove_choice(frontier, problem,s, process):
    if (problem.protype == 1): #sudoku
        pass
    elif(problem.protype == 2): #15puzzle
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
    

def SudokuHeuristic():
    pass
    
