import numpy as np
from node import node
import math
import copy

"""---------------------- Sudoku---------------------------"""
def sudoku_matrix(input, n):
    row = []
    sudoku = []
    d = 0
    for i in input: 
        row.append(i)
        d += 1 
        if (d%n == 0):
            sudoku.append(row)
            row = []
    return sudoku
    
def drawMatrix(matrix):
        print("")
        print("---------------------")
        print('\n'.join([''.join(['{:4}'.format(item) 
            for item in row]) for row in matrix]))
        print("---------------------")

def numArr(n):
    arr = []
    num = 1
    for x in range(n):
        arr.append(str(num))
        num = num +1
        
    return arr


def cajasEnMatrix(n):
    cantBox = n
    xi = 0
    xf = int(math.sqrt(n))
    yi = 0
    yf = int(math.sqrt(n))

    cajas = [[xi,xf,yi,yf]]

    while cantBox != 1:
        if(xi < n):
            yf = yf + int(math.sqrt(n))
            yi = yi + int(math.sqrt(n))
            if(yi == n):            
                yf = int(math.sqrt(n))
                yi = 0
                xf = xf + int(math.sqrt(n))
                xi = xi + int(math.sqrt(n))
        
        cantBox = cantBox -1
        cajas.append([xi,xf,yi,yf])

    return cajas

def foundCaja(cajas, p, n):
    point =  copy.deepcopy(p)
    point[0] = point[0] + 1
    point[1] = point[1] + 1
    for i in cajas:
        if cajas[cajas.index(i)][1] >= point[0] and cajas[cajas.index(i)][3] >= point[1]:
            return i

def noAccepted(s, n):
    if (len(s) != 16):
        print ("El tamaño no es el adecuado")
        return False
    
    for i in s:
        if (i != '.'):
            if (int(i) < 1 or int(i) > n):
                print("Algun numero no entra en el rango del sudoku")
                return False

    return True

    
"""----------------------- 15 Puzzle -----------------------"""
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

def move(tempS, matrix):
    nv = blanknode(tempS, 4, 0)
    ant = blanknode(matrix, 4, 0)
    if((ant.x -1) == nv.x):
        return "arriba"
    elif((ant.x +1) == nv.x):
        return "abajo"
    elif((ant.y -1) == nv.y):
        return "izquierda"
    elif((ant.y +1) == nv.y):
        return "derecha"

#Regresa TRUE si hay alguna igual
#Regresa False si no hay igual
def revExplored(explored, matrix):
    res = False
    for i in explored:
       # print("RESULT DE LA MATRIZ")
       # print(matrix)
       # print("EXPLORADO")
        #print(i)
        if (np.array_equal(matrix,i)):
            res = True
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
            print("arriba")
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
def change(m, nodVacio, nod2):
    matrix = m.copy()
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
            if (noAccepted(cadena, 4)):
                sudo = sudoku_matrix(cadena, 4)
                return 1, [sudo]
            return False
            select = False
        # 15 puzzle problem
        elif (problema == "2"):
            cadena = input("Ingrese el juego: \n")
            # el 2 indica el tipo de juego
            arrPuzzle = []
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
            return 2, arrPuzzle
            select = False
        else:
            print("Porfavor coloque una opcion valida")
            problema = input("Que juego desea solucionar. \n1.Sudoku \n2.15puzzle \n")
        

