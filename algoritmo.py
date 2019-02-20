def blankpuzzle(n, val):
    for x in range(n):
        for y in range (n):
            value = matrix[x,y]
            if value == val:
                return x,y

def AStart(problem):

    frontier = [[problem.initial]]
    explored = []

    while True:
        if len(frontier):
            path = remove_choice(frontier, problem.type)
            #s = path.end
            explored.appends(s)

            if(problem.goalTest(s)):
                return path

            for a in problem.actions(s):
                result = problem.result(s,a)
                if result[0] not in explored:
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
        
        
    pass

def SudokuHeuristic():
    pass
    
