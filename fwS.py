from funciones import *
from node import node
import copy
import math
import numpy as np


class framework():

     def __init__(self, initial, protype):
          self.initial = initial
          self.protype = protype
          self.cost =  0
          self.n = 4

     # regresa un array de arrays con 3 numeros (x,y,SudokuNum)
     def actions(self, matrix):
          a = 0
          position = []
          option = []

          # ver espacios libres
          for x in range(self.n):
               for y in range(self.n):
                    if matrix[x][y] == ".":
                         position.append(list([x,y]))

          #print(position)
          # posibles numeros en los espacios vacios
          while(a < len(position)):
               num = numArr(self.n)
               
               #row
               for i in range(self.n):
                    #print("posicion evaluada 1----------")
                    #print(matrix[position[a][0]][i])
                    if (matrix[position[a][0]][i] != "."):
                         num.remove(matrix[position[a][0]][i])

               #column
               for i in range(self.n):
                    #print("posicion evaluada 2")
                    #print(matrix[i][position[a][1]])
                    if ((matrix[i][position[a][1]] != ".") and (matrix[i][position[a][1]] in num)):
                         num.remove(matrix[i][position[a][1]])
               
               cajas = cajasEnMatrix(self.n)
               boxToRev = foundCaja(cajas,position[a], self.n)

               for w in range(boxToRev[0],boxToRev[1]):
                    for b in range(boxToRev[2],boxToRev[3]):
                         if (matrix[w][b] in num):
                              num.remove(matrix[w][b])
       
               option.append(num)
               a = a + 1                    
          
          res = []

          #creacion del array
          for c in range(len(position)):
              for i in option[c]:
                  action = copy.deepcopy(position[c])
                  action.append(i)
                  res.append(action)
                  action = []
          return res

     #remmplaza un numero en la posicion indicada          
     #regresa una matriz
     def result(self, s, a):
         temp = copy.deepcopy(s)
         temp[a[0]][a[1]] = a[2]

         return temp

     # verifica que los numeros no se repitan
     def goal_test(self, matrix):
          #row
          for x in range(self.n):
               goal = numArr(self.n)
               for y in range(self.n):
                    if (matrix[x][y] in goal):
                         goal.remove(matrix[x][y])
               if (len(goal) > 0):
                    return False
          
          #column
          for x in range(self.n):
               goal = numArr(self.n)
               for y in range(self.n):
                    if (matrix[y][x] in goal):
                         goal.remove(matrix[y][x])
               if (len(goal) > 0):
                    return False
          

          #box         
          cantBox = self.n
          xi = 0
          xf = int(math.sqrt(self.n))
          yi = 0
          yf = int(math.sqrt(self.n))
         
          while cantBox != 0:
               goal = numArr(self.n)
               for a in range(xi,xf):
                    for b in range(yi,yf):
                         if (matrix[a][b] in goal):
                              goal.remove(matrix[a][b])

               if (len(goal) > 0):
                    return False
               if(xi < self.n):
                    yf = yf + int(math.sqrt(self.n))
                    yi = yi + int(math.sqrt(self.n))
                    if(yi == self.n):
                         yf =  int(math.sqrt(self.n))
                         yi = 0
                         xf = xf + int(math.sqrt(self.n))
                         xi = xi + int(math.sqrt(self.n))
               cantBox = cantBox -1
               
          
          return True
     
     #costo por acción
     def stepCost(self,s,a,s2):
        self.cost += 1

     #costo de todas las acciones
     def pathCost(self,statesList):
        return len(statesList)

    
    
