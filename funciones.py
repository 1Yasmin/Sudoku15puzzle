import numpy as np
from node import node

# crea una matriz de leng n*n apartir de un array
def createMatrix(n,arr):
    matrix = np.zeros((n,n))
    arrval = 0
    for x in range(n):
        for y in range (n):
            matrix[x,y] = arr[arrval]
            arrval = arrval +1
    return matrix
#uso de createMatrix
#createMatrix(4, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])

def newFrontier(s,a):   
    vacio = blanknode(s,4,0)
    if(a == "arriba"):
        return node(vacio.x-1,vacio.y)                        
    if(a == "abajo"):
        return node(vacio.x+1,vacio.y)         
    if(a == "izquierda"):
        return node(vacio.x,vacio.y-1)       
    if(a == "derecha"):
        return node(vacio.x,vacio.y+1)            

def getGoal(n):
    matrix = np.zeros((n,n))
    arrval = 1
    for x in range(n):
        for y in range (n):
            if(y == n-1 and x == n-1):
                matrix[x,y] = 0
            else:
                matrix[x,y] = arrval
                arrval = arrval +1
    return matrix

def blanknode(matrix, n, val):
    for x in range(n):
        for y in range (n):
            value = matrix[x,y]
            if value == val:
                return node(x,y)

def revExplored(explored, matrix):
    res = True
    for i in range(len(explored)):
        if not (np.array_equal(matrix,i)):
            res = True
        else:
            res = False
    return res
    
            
#busca los nodos alrededor de la posicion en blanco 
def getInitial(matrix, n, val):
    vacio = blanknode(matrix,n,val)
    #para el puzzle
    actions = []
    #nodo de arriba
    try:
        if ((vacio.x-1) >= 0 and (vacio.x-1) < 4):
            arriba = node(vacio.x-1, vacio.y)
            actions.append(arriba)
    except IndexError:
        pass
    #nodo de abajo
    try:
        if ((vacio.x+1) >= 0 and (vacio.x+1) < 4):
            arriba = node(vacio.x+1, vacio.y)
            actions.append(arriba)
    except IndexError:
        pass
    #nodo de la izquierda
    try:
        if ((vacio.y-1) >= 0 and (vacio.y-1) < 4):
            izquierda = node(vacio.x,vacio.y-1)
            actions.append(izquierda)
    except IndexError:
        pass
    #nodo de la derecha
    try:
        if ((vacio.y+1) >= 0 and (vacio.y+1) < 3):
            derecha = node(vacio.x, vacio.y+1 )
            actions.append(derecha)
    except IndexError:
        pass
    return actions

    

# movimiento del cuadro
def change(matrix, nodVacio, nod2):
    num = matrix[nod2.x, nod2.y]
    matrix[nodVacio.x,nodVacio.y] = num
    matrix[nod2.x, nod2.y] = 0
    return matrix
       

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
        

