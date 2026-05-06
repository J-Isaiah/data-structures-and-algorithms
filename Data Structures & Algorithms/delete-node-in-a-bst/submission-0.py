# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right =  self.deleteNode(root.right,key)
        elif root.val > key: 
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left and not root.right:
                return None
            elif root.right and root.left:
                root.right.left = root.left
                return root.right
            elif root.left:
                return root.left
            elif root.right:
                return root.right


        return root

        