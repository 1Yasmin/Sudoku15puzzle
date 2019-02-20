import numpy as np


def createMatrix(n,arr):
    matrix = np.zeros((n,n))
    arrval = 0
    for x in range(n):
        for y in range (n):
            matrix[x,y] = arr[arrval]
            arrval = arrval +1
    return matrix

#uso de createMatrix
createMatrix(4, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])

# Menu de inicio
def selectProblem():
    problema = input("Que juego desea solucionar. \n1.Sudoku \n2.15puzzle \n")
    select = True

    while select:
        # Sudoku problem
        
        if (problema == "1"):
            cadena = input("Ingrese el juego: \n")
            
            select = False
        # 15 puzzle problem
        elif (problema == "2"):
            cadena = input("Ingrese el juego: \n")
            # el 2 indica el tipo de juego
            arrPuzzle = [2]
            #guardar valores en una lista
            for i in cadena:
                if i != ".":
                    num = int(i, 16)
                    arrPuzzle.append(num)
                elif i == ".":
                    arrPuzzle.append(0)
                else:
                    "Error en la entrada"
            #print (arrPuzzle)
            return arrPuzzle
            select = False
        else:
            print("Porfavor coloque una opcion valida")
            problema = input("Que juego desea solucionar. \n1.Sudoku \n2.15puzzle \n")
        

