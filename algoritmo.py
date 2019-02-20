def AStart(problem):

    frontier = [[problem.initial]]
    explored = []

    while True:
        if len(frontier):
            path = remove_choice(frontier)
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
            
    
