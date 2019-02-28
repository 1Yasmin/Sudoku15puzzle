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
        problem = fwS.framework(entrada, protype)
        AStart(problem)
      #  print(problem.actions([['2','4','.','1'],['3','1','4','2'],['1','.','.','4'],['4','2','1','.']]))
        
    elif(protype == 2):
        matrixInicial = createMatrix(4,entrada)
        problem = fw.frameWork(matrixInicial, getInitial(matrixInicial,4,0), getGoal(4), protype)
        AStart(problem)
        

main()


