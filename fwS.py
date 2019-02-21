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
          pass

     def goal_test(self, matrix):
          "Define goal test"
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

    
    
