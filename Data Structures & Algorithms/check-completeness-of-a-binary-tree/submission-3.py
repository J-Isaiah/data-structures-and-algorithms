# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            seen_nul =False 
            q = deque()
            q.append(root)

            while q and status:
                cur = q.popleft()

                if cur is None:
                    seen_nul = False
                else:
                    if seen_nul:
                        return False
                    q.append(cur.left)
                    q.append(cur.right)



                

                q.append(cur.left)
                q.append(cur.right)
            return True

        return bfs(root)
