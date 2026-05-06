# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def search(node, target):

            if not node:
                return False 
            dif = target - node.val 


            if not node.left and not node.right and dif == 0:
                return True

            if search(node.left, dif) or search(node.right, dif):
                return True
            return False
        return search(root,targetSum)



                

        