

def AStart(problem):
    #nodos cercanos
    frontier = [[problem.initial]]
    #estados prima guardados
    explored = []

    while True:
        if len(frontier):
            #devuelve el nodo que debe moverse
            path = remove_choice(frontier, problem.type)
            #estado de la matriz dado el path
            s = path.end 
            explored.appends(s)

            if(problem.goalTest(s)):
                return path
            
            for a in problem.actions(s):
                result = problem.result(s,a)
                if result not in explored:
                        # nodo que se va a mover
                        new_path = []
                        new_path.extend(path)
                        new_path.extend(problem.result(s,a))
                        frontier.append(new_path)
            else:
                return False    



def remove_choice(frontier, type):
    if (problem.type == 1): #sudoku
        pass
    elif(problem.type == 2): #15puzzle
        pass

        
    

def PuzzleHeuristic():
    """
 
        """
        
    pass

def SudokuHeuristic():
    pass
    
