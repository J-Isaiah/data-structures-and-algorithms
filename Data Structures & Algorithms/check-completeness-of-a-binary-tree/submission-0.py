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
            status = True
            q = deque()
            q.append(root)

            while q and status:
                cur = q.popleft()

                if not cur or not cur.left and not cur.right:
                    continue
                if not cur.left and cur.right:
                    status = False
                    break
                

                q.append(cur.left)
                q.append(cur.right)

            return status

        return bfs(root)
