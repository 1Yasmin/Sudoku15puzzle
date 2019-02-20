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
            if ((s.y-1) > 0 and (s.y-1) < 4):
                actions.append("izquierda")
        except IndexError:
            pass
        #Mover hacia la derecha
        try:
            if ((s.y+1) >= 0 and (s.y+1) < 3):
                actions.append("derecha")
        except IndexError:
            pass
        print (actions)

    def result(self,s,a):
        pass
    
    def goalTest(self,s):
        if(s in self.goal):
            return True
        else:
            return False
        
    def stepCost(self,s,a,s2):
        self.cost += 1

    def pathCost(self,statesList):
        return len(statesList) 
