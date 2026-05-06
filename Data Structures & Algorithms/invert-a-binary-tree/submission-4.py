# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        if not root.right and not root.left:
            return root
        
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.right = right
        root.left = left 
        return root