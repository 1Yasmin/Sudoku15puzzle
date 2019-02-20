class frameWork():

    def __init__(self,initial,goal,type):
        self.initial = initial
        self.type = type
        self.cost =  0
        self.goal = goal

    def actions(self,s):
        #para el puzzle
        actions = []
        #Mover hacia arriba
        """try:
            if (self.matrix[x+1][y].color==(255,255,255) or self.matrix[x+1][y].color==(255,0,0) or self.matrix[x+1][y].color==(0,255,0)):
                actions.append("derecha")
        except IndexError:
            pass
        #Mover hacia abajo
        #Mover hacia la izquierda
        #Mover hacia la derecha
        
"""
        pass
    
    def result(self,s,a):
        pass
    
    def goalTest(self,s):
        if(s in self.goal):
            return True
        return False
        
    def stepCost(self,s,a,s2):
        self.cost += 1

    def pathCost(self,statesList):
        return len(statesList) 
