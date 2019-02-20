# Programa principal para el sudoku y 15 puzzle
from funciones import *
from node import node
from algoritmo import AStart
import fw

def main():
    entrada = selectProblem()
    type = entrada[0]
    matrixInicial = createMatrix(4,entrada[1:])

    print(matrixInicial)
    problem = fw.frameWork(matrixInicial, getInitial(matrixInicial,4,0), [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0], type)

    print(problem.result(matrixInicial, "izquierda"))
#pruebas de la 
    #nod = node(0,3)
    #problem.actions(nod)
    #print(problem.goalTest([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]))

#    nodos iniciales
    """
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

    
   # AStart(problem)


main()

