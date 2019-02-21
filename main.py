# Programa principal para el sudoku y 15 puzzle
from funciones import *
from node import node
from algoritmo import AStart
import fw
import fwS
import numpy as np

def main():
    protype, entrada = selectProblem()

    if (protype == 1):
        print (drawMatrix(entrada))
        problem = fwS.framework(entrada, protype)
        AStart(problem)
        
    elif(protype == 2):
        matrixInicial = createMatrix(4,entrada)
        problem = fw.frameWork(matrixInicial, getInitial(matrixInicial,4,0), getGoal(4), protype)
        print(matrixInicial)
        AStart(problem)
        
        




    """
    nod = node(2,1)
    nod2 = node(2,2)
    arr = []
    print("...................")
    a = change(matrixInicial,nod , nod2)
    arr.append(a) 
    print(arr)
    #pruebas de la
    #print(problem.result(matrixInicial, "derecha"))
    #print(getGoal(4))
    #nod = node(0,3)
    #problem.actions(nod)
    print(problem.goalTest())
    print(getGoal(4))
    print(problem.goalTest(matrixInicial))


#    nodos iniciales

    hi = getInitial(matrixInicial,4,0)
    print(hi[0].x)
    print(hi[0].y)
    print(hi[1].x)
    print(hi[1].y)
    print(hi[2].x)
    print(hi[2].y)
    print(hi[3].x)
    print(hi[3].y)
    print(len(hi)) """

    
   


main()

