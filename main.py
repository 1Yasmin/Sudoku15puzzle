# Programa principal para el sudoku y 15 puzzle
from funciones import *
from node import node
from algoritmo import AStart
import fw
import fwS
import numpy as np


#F21C856B49A73ED.


def main():
    if(selectProblem() != False):
        protype, entrada = selectProblem()
        if (protype == 1):
            problem = fwS.framework(entrada, protype)
            AStart(problem)      
        
        elif(protype == 2):
            matrixInicial = createMatrix(4,entrada)
            print(matrixInicial)
            problem = fw.frameWork(matrixInicial, getInitial(matrixInicial,4,0), getGoal(4), protype)
            AStart(problem)
            

main()


