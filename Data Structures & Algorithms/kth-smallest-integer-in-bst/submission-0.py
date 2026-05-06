# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output_array = self.IOT(root)
        return output_array[k-1]
    
    def IOT(self, root,):
        if not root:
            return []

        return self.IOT(root.left) + [root.val] +self.IOT(root.right)

            

        
        

        