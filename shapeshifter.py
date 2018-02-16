# coding=utf-8

import search

class ShapeShifterSearchProblem():
    def __init__(self, pieces, gamemap, numranks):
        self.startState = (pieces, gamemap)
        self.numranks = numranks
        self._expanded = 0 # number of nodes expanded

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        """Checks if state is goal"""
        for row in state[1]:
            for c in row:
                if c != 0:
                    return False
        return len(state[0]) == 0

    def getSuccessors(self, state):
        """
        Returns legal moves and child states from a state
        """
        numranks = self.numranks
        piecesleft, gamemap = state
        #print 'state =',state
        #print 'piecesleft =',piecesleft
        if len(piecesleft) == 0: return []
        #print 'piecesleft[0] =',piecesleft[0]
        piecesleft = list(piecesleft)
        successors = []
        dimensions, piece = piecesleft[0]
        piecewidth, pieceheight = dimensions
        piece = [list(row) for row in piece]
        mapwidth = len(gamemap[0])
        mapheight = len(gamemap)

        for j in range(mapheight - pieceheight + 1):
            for i in range(mapwidth - piecewidth + 1):
                newmap = [list(row) for row in gamemap]
                for n in range(pieceheight):
                    for m in range(piecewidth):
                        newmap[n + j][m + i] = (newmap[n + j][m + i] + piece[n][m]) % numranks
                newmap = tuple([tuple(row) for row in newmap])
                successors.append(((tuple(piecesleft[1:]), newmap), (i,j), 1))

        self._expanded += 1
        #print 'successors =',successors
        return successors

    def getCostOfActions(self, actions):
        """
        Uniform cost
        """
        return len(actions)

def shapeshifterHeuristic(state, problem):
    """
    Heuristic for the game
    """
    piecesleft, gamemap = state
    return sum(sum([bool(y != 0) for y in x]) for x in gamemap)




#Example board
SHAPESHIFTER_DATA = ((2,0,0,2), (1,1,1,0), (1,1,0,2), (0,1,2,1))

if __name__ == "__main__":

    # pieces = (
    #     ((3, 3), ((1, 1, 1, 0), (1, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0))),  #upsdwn L
    #     ((3, 3), ((1, 0, 0, 0), (1, 1, 1, 0), (0, 0, 1, 0), (0, 0, 0, 0))),  #grub screw
    #     ((2, 2), ((1, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  #square
    #     ((3, 3), ((1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 0), (0, 0, 0, 0))),  #french fry
    #     ((3, 3), ((1, 1, 0, 0), (1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0))),  #q
    #     ((3, 3), ((1, 1, 1, 0), (0, 1, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0))),  #エ
    #     ((2, 3), ((1, 1, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0))),  #bckwrd c
    #     ((3, 3), ((1, 1, 1, 0), (1, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0))),  #upsdwn L
    #     ((3, 2), ((1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # -\_
    #     ((2, 3), ((1, 1, 0, 0), (1, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0))),  #ビル
    #     ((3, 3), ((1, 0, 0, 0), (1, 1, 1, 0), (1, 0, 0, 0), (0, 0, 0, 0))),  #|--
    # )
    # pieces = (
    #     ((3, 3), ((1, 1, 1, 0), (1, 0, 1, 0), (1, 1, 1, 0), (0, 0, 0, 0))),  # ring
    #     ((3, 2), ((1, 1, 1, 0), (0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # short T
    #     ((2, 3), ((0, 1, 0, 0), (1, 1, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0))),  # -|
    #     ((2, 3), ((1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0))),  # |-
    #     ((2, 2), ((0, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # _|
    #     ((2, 2), ((1, 1, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # ‾|
    #     ((3, 3), ((0, 1, 1, 0), (0, 1, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0))),  # bckwrd ユ
    #     ((3, 3), ((0, 0, 1, 0), (0, 1, 1, 0), (1, 1, 1, 0), (0, 0, 0, 0))),  # 右階段
    #     ((3, 3), ((1, 0, 0, 0), (1, 1, 1, 0), (0, 0, 1, 0), (0, 0, 0, 0))),  # grub screw
    #     ((2, 3), ((1, 0, 0, 0), (1, 1, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0))),  # 左蛞蝓
    #     ((3, 3), ((0, 1, 0, 0), (1, 1, 1, 0), (0, 1, 0, 0), (0, 0, 0, 0))),  # +
    # )


    #Manually create list of pieces for now
    pieces = (
        ((2, 2), ((1, 1, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # ‾|
        ((3, 3), ((0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 0, 0), (0, 0, 0, 0))),  # bckwrd grub screw
        ((3, 3), ((1, 1, 1, 0), (1, 0, 1, 0), (1, 1, 1, 0), (0, 0, 0, 0))),  # ring
        ((2, 1), ((1, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # -
        ((3, 2), ((1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # zig2
        ((2, 3), ((1, 1, 0, 0), (1, 1, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0))),  # ビル
        ((1, 2), ((1, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # l
        ((3, 3), ((1, 1, 1, 0), (0, 1, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0))),  # エ
        ((3, 3), ((1, 1, 0, 0), (1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0))),  # q
        ((2, 3), ((1, 1, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0))),  # 1‾
        ((3, 3), ((0, 1, 0, 0), (1, 1, 1, 0), (0, 1, 0, 0), (0, 0, 0, 0))),  # +
        ((3, 2), ((0, 1, 1, 0), (1, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0))),  # van
    )


    gamemap = SHAPESHIFTER_DATA
    problem = ShapeShifterSearchProblem(pieces, gamemap, 3)
    path = search.aStarSearch(problem, heuristic=shapeshifterHeuristic) #takes ~30 seconds
    print 'path =',path
    print problem._expanded, "nodes expanded"

