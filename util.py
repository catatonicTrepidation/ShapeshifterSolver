"""Provided by Berkeley"""

import heapq

class PriorityQueue:
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

class PriorityQueueWithFunction(PriorityQueue):
    def  __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )
