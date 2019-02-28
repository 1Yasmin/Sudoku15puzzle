from funciones import *
from node import node
import numpy as np

class frameWork():

    def __init__(self, matrix,initial,goal,protype):
        self.matrix = matrix
        self.initial = initial
        self.protype = protype
        self.cost =  0
        self.goal = goal
        self.n = 4
        
    # s es un nodo
    def actions(self,state):
        s = blanknode(state,self.n,0)
        #para el puzzle
        actions = []
        #Mover hacia arriba
        try:
            if ((s.x-1) >= 0 and (s.x-1) < self.n):
                actions.append("arriba")
        except IndexError:
            pass
        #Mover hacia abajo
        try:
            if ((s.x+1) >= 0 and (s.x+1) < self.n):
                actions.append("abajo")
        except IndexError:
            pass
        #Mover hacia la izquierda
        try:
            if ((s.y-1) >= 0 and (s.y-1) < self.n):
                actions.append("izquierda")
        except IndexError:
            pass
        #Mover hacia la derecha
        try:
            if ((s.y+1) >= 0 and (s.y+1) < (self.n-1)):
                actions.append("derecha")
        except IndexError:
            pass
        return actions

    # s es una matriz
    # a es una accion
    def result(self,s,a):
        vacio = blanknode(s,self.n,0)
        matriz = s.copy()
        if(a == "arriba"):
            nod = node(vacio.x-1,vacio.y)
            matriz = change(s, vacio, nod)                        
        if(a == "abajo"):
            nod = node(vacio.x+1,vacio.y)
            matriz = change(s, vacio, nod)            
        if(a == "izquierda"):
            nod = node(vacio.x,vacio.y-1)
            matriz = change(s, vacio, nod)            
        if(a == "derecha"):
            nod = node(vacio.x,vacio.y+1)
            matriz = change(s, vacio, nod)            
        return matriz

    #Verifica que la matriz este ordenada
    #s es una matriz
    def goalTest(self,s):
        if(np.array_equal(s,self.goal)):
            return True
        else:
            return False
        
    def stepCost(self,s,a,s2):
        self.cost += 1

    def pathCost(self,statesList):
        return len(statesList) 
