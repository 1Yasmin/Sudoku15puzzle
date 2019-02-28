from funciones import *
from node import node
import copy
import math

def AStart(problem):
    #1.matrices
    #2.nodos cercanos
    frontier = problem.initial
    #estados prima guardados
    explored = []
        
    while True:
           
        if len(frontier):

            if(problem.protype == 1):
                path = remove_choice(frontier, problem, explored)
                state= path
                explored.append(state)
                
                #next state
                drawMatrix(state)
                
                #Test
                if problem.goal_test(state):
                    return path
                
                for a in problem.actions(state):
                   # print(a)
                    result = problem.result(state, a)
                    
                    if result not in explored:
                        frontier.append(result)
                    #frontier.append(result)

                #print (frontier)

            if(problem.protype == 2):
                
                #devuelve el nodo que debe moverse
                path = remove_choice(frontier, problem, explored)
                #estado de la matriz dado el path
                s = change(problem.matrix, blanknode(problem.matrix,4,0), path)
                tempS = s.copy()
                explored.append(tempS)
                problem.matrix = s
                
                if(problem.goalTest(s)):
                    return True

                frontier = []

                print("- Next State-")
                print(s)

                for a in problem.actions(s):
                    temp = s.copy()
                    result = problem.result(temp,a)
                    if (revExplored(explored, result) == False):
                        # nodo que se va a mover
                        new_path = newFrontier(s,a)
                        frontier.append(new_path)
        else:
            return False   


def remove_choice(frontier, problem, explored):
    if(problem.protype == 1):
        posibles = []
        for i in frontier: 
            posibles.append(sudokuHeuristic(i, problem, explored))

        return frontier[posibles.index(min(posibles))]
    
    
def sudokuHeuristic(matrix, problem, explored):
    vacio = 0
    #row
    for x in range(problem.n):
        for y in range(problem.n):
            if (matrix[x][y] == "."):
                vacio = vacio +1
    #column
    for x in range(problem.n):
        goal = numArr(problem.n)
        for y in range(problem.n):
            if (matrix[y][x] == "."):
                vacio == "."
    #box
    cantBox = problem.n
    xi = 0
    xf = int(math.sqrt(problem.n))
    yi = 0
    yf = int(math.sqrt(problem.n))
    
    while cantBox != 0:
        #print(cantBox)
        for a in range(xi,xf):
            for b in range(yi,yf):
                if (matrix[a][b] == "."):
                    vacio = vacio + 1

        if(xi < problem.n):
            yf = yf + int(math.sqrt(problem.n))
            yi = yi + int(math.sqrt(problem.n))
            if(yi == problem.n):
                yf =  int(math.sqrt(problem.n))
                yi = 0
                xf = xf + int(math.sqrt(problem.n))
                xi = xi + int(math.sqrt(problem.n))

        cantBox = cantBox -1
        #print (xi, xf, yi, yf)


    val = problem.pathCost(explored) + vacio
    return val
    
    
def PuzzleHeuristic(nod, problem, explored):
    misplace = 0
    res = change(problem.matrix, blanknode(s,4,0),nod)
   
    for x in range(4):
        for y in range (4):
            value1 = s[x,y]
            value2 = res[x,y]
            if value1 != value2:
                misplace = misplace+1
                
    val = problem.pathCost(explored) + misplace
    return val
    
