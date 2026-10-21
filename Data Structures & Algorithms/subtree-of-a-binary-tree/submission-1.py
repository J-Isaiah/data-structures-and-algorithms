# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return False

            if root.val == subRoot.val:
                outcome = bfs(root, subRoot)
                if outcome:
                    return True
            return dfs(root.left) or dfs(root.right)

            

        def bfs(r1, r2):
            q1 = collections.deque([r1]) 
            q2 = collections.deque([r2]) 

            while q1 and q2:
                n1 = q1.popleft()
                n2 = q2.popleft()

    
                if n1 is None and n2 is None:
                    continue
                
                if n1 is None or n2 is None:
                    return False
                
                if n1.val != n2.val:
                    return False

                q1.append(n1.left)
                q2.append(n2.left)
                        
                q1.append(n1.right)
                q2.append(n2.right)
            return True
            
        return dfs(root)


            
        