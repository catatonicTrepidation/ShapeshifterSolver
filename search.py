import util

def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    startstate = problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push((startstate,[]), heuristic(startstate, problem))
    explored = set()
    while not frontier.isEmpty():
        parentstate, prevactions = frontier.pop()
        if problem.isGoalState(parentstate):
            return prevactions
        if parentstate not in explored:
            explored.add(parentstate)
            for childstate, action, cost in problem.getSuccessors(parentstate):
                frontier.push((childstate, prevactions + [action]), problem.getCostOfActions(prevactions + [action]) + heuristic(childstate, problem))
    return []