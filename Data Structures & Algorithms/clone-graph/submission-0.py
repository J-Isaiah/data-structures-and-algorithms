"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        def bfs(node):
            if not node:
                return None
            seen = set()
            old_to_new = {}
            q = collections.deque()
            q.append(node)

            while q:
                cur = q.popleft()
                if cur not in old_to_new:
                    old_to_new[cur] = Node(val=cur.val, neighbors=[])
                
                if cur in seen:
                    continue
                
                seen.add(cur)

                new_node = old_to_new[cur]

                neighbors = cur.neighbors

                for neighbor in neighbors:
                    q.append(neighbor)
                    if neighbor not in old_to_new:
                        old_to_new[neighbor] = Node(val=neighbor.val, neighbors=[])
                    
                    new_node.neighbors.append(old_to_new[neighbor])

            return old_to_new[node]

        return bfs(node)
