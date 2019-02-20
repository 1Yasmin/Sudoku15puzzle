from funciones import *
from node import node

class frameWork():

    def __init__(self, matrix,initial,goal,type):
        self.matrix = matrix
        self.initial = initial
        self.type = type
        self.cost =  0
        self.goal = goal
        
    # s es un nodo
    def actions(self,s):
        #para el puzzle
        actions = []
        #Mover hacia arriba
        try:
            if ((s.x-1) >= 0 and (s.x-1) < 4):
                actions.append("arriba")
        except IndexError:
            pass
        #Mover hacia abajo
        try:
            if ((s.x+1) >= 0 and (s.x+1) < 4):
                actions.append("abajo")
        except IndexError:
            pass
        #Mover hacia la izquierda
        try:
            if ((s.y-1) >= 0 and (s.y-1) < 4):
                actions.append("izquierda")
        except IndexError:
            pass
        #Mover hacia la derecha
        try:
            if ((s.y+1) >= 0 and (s.y+1) < 3):
                actions.append("derecha")
        except IndexError:
            pass
        return actions

    # s es una matriz
    # a es una accion
    def result(self,s,a):
        vacio = blanknode(s,4,0)
        if(a == "arriba"):
            nod = node(vacio.x-1,vacio.y)
            s = change(s, vacio, nod)                        
        if(a == "abajo"):
            nod = node(vacio.x+1,vacio.y)
            s = change(s, vacio, nod)            
        if(a == "izquierda"):
            nod = node(vacio.x,vacio.y-1)
            s = change(s, vacio, nod)            
        if(a == "derecha"):
            nod = node(vacio.x,vacio.y+1)
            s = change(s, vacio, nod)            
        return s

    #Verifica que la matriz este ordenada
    #s es una matriz
    def goalTest(self,s):
        if(s == self.goal):
            return True
        else:
            return False
        
    def stepCost(self,s,a,s2):
        self.cost += 1

    def pathCost(self,statesList):
        return len(statesList) 
