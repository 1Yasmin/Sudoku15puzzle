# Programa principal para el sudoku y 15 puzzle
from funciones import *
from node import node
from algoritmo import AStart
import fw
import fwS
import numpy as np


#2468ACE.13579BDF


def main():
    protype, entrada = selectProblem()

    if(protype != 0):
        if (protype == 1):
            problem = fwS.framework(entrada, protype)
            AStart(problem)      
        
        elif(protype == 2):
            matrixInicial = createMatrix(4,entrada)
            problem = fw.frameWork(matrixInicial, getInitial(matrixInicial,4,0), getGoal(4), protype)
            AStart(problem)
            

main()


