from funciones import *
from node import node
import copy
import numpy as np


class framework():

     def __init__(self, initial, protype):
          self.initial = initial
          self.protype = protype
          self.cost =  0
          self.n = 4

     def actions(self, matrix):
          empty = 0
          n = 0
          m = 0
          position = []
          possibility = []
          poss_matrix = []

          for x in range(self.n):
               for y in range(self.n):
                    if matrix[x][y] == ".":
                         position.append(tuple([x,y]))
                         empty += 1
                         
          while(n < empty):
               num = ["1", "2", "3", "4"]
               for i in range(self.n):
                    if (matrix[position[n][0]][i] != "."):
                         num.remove(matrix[position[n][0]][i])

               for i in range(self.n):
                    if ((matrix[i][position[n][1]] != ".") and (matrix[i][position[n][1]] in num)):
                         num.remove(matrix[i][position[n][1]])
               possibility.append(num)
               n += 1

          while(m < empty):
               for i in possibility[m]:
                    temp = copy.deepcopy(matrix)
                    temp[position[m][0]][position[m][1]] = i
                    poss_matrix.append(temp)
               m += 1
          return poss_matrix 

     def goal_test(self, matrix):
          "Define goal test"
          #[1, 2, 3, 4] appear exactly once in each row, column and box
          #row
          for x in range(self.n):
               goal = ["1", "2", "3", "4"]
               for y in range(4):
                    if (matrix[x][y] in goal):
                         goal.remove(matrix[x][y])
          if (len(goal) > 0):
               return False

          #column
          for x in range(self.n):
               goal = ["1", "2", "3", "4"]
               for y in range(4):
                    if (matrix[y][x] in goal):
                         goal.remove(matrix[y][x])
               if (len(goal) > 0):
                    return False

          a, b, c, i= (0,)*4
          while (i < self.n):
               if(i==1):
                    a = 2
               elif (i==2):
                    a = 0
                    b = 2
               elif (i==3):
                    a = 2
                    b = 2
               for x in range(2):
                    for y in range(2):
                         if (matrix[x+b][y+a] in goal):
                              goal.remove(matrix[x+b][y+a])
               if(len(goal) != 0):
                    return False
          return True

    
    
