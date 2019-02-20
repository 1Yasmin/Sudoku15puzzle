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
    problem = fw.frameWork(entrada[1:], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0], type)

    nod = node(False, 0,0)
    problem.actions(nod)
    
   # AStart(problem)


main()

