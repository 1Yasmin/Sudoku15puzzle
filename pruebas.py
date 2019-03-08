from funciones import *
import copy
import math
"""
a = createMatrix(4,[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,3])  #igual a f
b = createMatrix(4,[1,2,3,4,5,6,7,8,9,1,5,3,2,2,6,2])
c = createMatrix(4,[1,2,3,4,1,2,3,3,2,1,2,3,4,5,6,15])  #igual a G
d = createMatrix(4,[1,5,2,2,3,5,7,8,9,2,3,5,6,5,9,7])
e = createMatrix(4,[1,2,3,4,5,6,7,4,4,5,6,4,5,6,7,8])
f = createMatrix(4,[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,3])
g = createMatrix(4,[1,2,3,4,1,2,3,3,2,1,2,3,4,5,6,15])

explored = []

explored.append(a)
explored.append(b)
explored.append(c)
explored.append(d)

print(explored)

print(revExplored(explored, g))

goal = numArr(9)
x = 0
while x < 9:
    print("hola")
    x = x+3
    
matrix=[['1','5','4','6','9','3','2','8','7'],['6','3','2','5','7','8','9','4','1'],['8','9','7','1','2','4','6','5','3'],['5','1','9','8','4','7','3','2','6'],['2','4','3','9','6','5','7','1','8'],['7','6','8','3','1','2','4','9','5'],['4','8','6','7','5','9','1','3','2'],['9','7','5','2','3','1','8','6','4'],['3','2','1','4','8','6','5','7','9']]

cantBox = 9
xi = 0
xf = 3
yi = 0
yf = 3

while cantBox != 0:
    goal = numArr(9)
    for a in range(xi,xf):
        for b in range(yi,yf):
            #print(a,b)
            #print(matrix[a][b])
            #print(goal)
            if (matrix[a][b] in goal):
                goal.remove(matrix[a][b])
                
                            
    if (len(goal) > 0):
        print("no")

    
    if(xi < 9):
        yf = yf + int(math.sqrt(9))
        yi = yi + int(math.sqrt(9))
        if(yi == 9):            
            yf = 3
            yi = 0
            xf = xf + int(math.sqrt(9))
            xi = xi + int(math.sqrt(9))
    print("index")
    print(xi,xf, yi,yf)
    
    cantBox = cantBox -1
        

b = [[[1,2,3],[2,3,4]], [[1,4,3],[2,5,6,7]]]
a = [[[1,2,3],[2,3,4]]]
for x in b:
    print(x)


    
matrix=[['1','5','4','6','9','3','2','8','7'],['6','3','2','5','7','8','9','4','1'],['8','9','7','1','2','4','6','5','3'],['5','1','9','8','4','7','3','2','6'],['2','4','3','9','6','5','7','1','8'],['7','6','8','3','1','2','4','9','5'],['4','8','6','7','5','9','1','3','2'],['9','7','5','2','3','1','8','6','4'],['3','2','1','4','8','6','5','7','9']]

point = [7,1]


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

print (cajasEnMatrix(4))
          

#print(foundCaja(cajas,point))


a = ['1','2','3','4','5']
if lalala != '.':
    if lalala in num:
        num.remove(lalala)

"""
"""
matriz = [['.', '4', '.', '1'], ['3', '.', '4', '.'], ['1', '.', '.', '4'], ['.', '2', '1', '.']]

matriz[0][0]
"""

2  4  6  8
10 12 14 0
1  3  5  7
9  11 13 15

2  4  6  8
10 12 14 0
1  3  5  7
9  11 13 15

2  4  6  0
10 12 14 8
1  3  5  7
9  11 13 15

2  4  6  8
10 12 14 0
1  3  5  7
9  11 13 15

2  4  0  6
10 12 14 8
1  3  5  7
9  11 13 15

2  0  4  6  
10 12 14 8
1  3  5  7
9  11 13 15

0  2  4  6  
10 12 14 8
1  3  5  7
9  11 13 15

10 2  4  6  
0  12 14 8
1  3  5  7
9  11 13 15







