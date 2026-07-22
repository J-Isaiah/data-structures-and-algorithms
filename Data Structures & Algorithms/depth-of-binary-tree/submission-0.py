# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def dfs(root, depth):
            r = l = depth

            if not root or not root.right or not root.left:
                return 0
            if root.right: 
                r+=dfs(root.right,depth+1)
        
            if root.left:
                l+=dfs(root.left,depth+1)
            return max(r,l)

        return dfs(root,1)