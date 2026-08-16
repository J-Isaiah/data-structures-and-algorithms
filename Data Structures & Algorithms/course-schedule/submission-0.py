class Node:
    def __init__(self, val=None, neighbors=[], state=0):
        self.val = val
        self.neighbors = neighbors
        self.state = state


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a list

        adjList = {}
        for c1, c2 in prerequisites:
            if c1 not in adjList:
                adjList[c1] = Node(c1)
            if c2 not in adjList:
                adjList[c2] = Node(c2)

            adjList[c2].neighbors.append(adjList[c1])

        # Algorithem
        def dfs(node):
            for neighbor in node.neighbors:
                if neighbor.state == 1:
                    return False

                neighbor.state = 1

                next = dfs(neighbor)
            neighbor.state = 2
            return True

        for value in adjList.values():
            if not dfs(value):
                return False

        return True
