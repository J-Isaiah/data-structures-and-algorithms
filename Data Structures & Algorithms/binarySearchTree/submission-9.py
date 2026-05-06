from collections import deque
class Node:
    def __init__(self, key, val=-1, right=None, left=None):
        self.val = val 
        self.key = key
        self.right = right
        self.left = left
class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        new_node = Node(key, val)
        if not self.root:
            self.root = new_node
            return 
        
        self.insert_helper(new_node, self.root )
    def insert_helper(self,new_node, root):
        if not root:
            return new_node

        if new_node.key > root.key:
            root.right = self.insert_helper(new_node, root.right)
        elif new_node.key < root.key:
            root.left = self.insert_helper(new_node, root.left)
        elif new_node.key == root.key:
            #replace node if key same
            root.val = new_node.val
        
        return root
        





    def get(self, key: int) -> int:
        return self.get_helper(key, self.root)


    
    def get_helper(self, key, root=None):
        if not root:
            return -1
        
        if root.key < key:
            return self.get_helper(key, root.right)
        elif root.key > key:
            return self.get_helper(key, root.left)
        elif root.key == key:
            return root.val
        else:
            return -1






    def getMin(self) -> int:
        root = self.root
        if not root:
            return -1
        
        while root.left:
            root = root.left

        return root.val


        


    def getMax(self) -> int:
        root = self.root

        if not root:
            return -1

        while root.right:
            root = root.right
        return root.val


    def remove(self, key: int) -> None:
        self.root = self.remove_helper(key, self.root)

    def remove_helper(self, key, root):
        if not root:
            return None
        if root.key > key:
            root.left = self.remove_helper(key, root.left)
        elif root.key < key:
            root.right = self.remove_helper(key, root.right )
        elif root.key == key:
            if root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right 
            elif not root.right and not root.left:
                return None
            else:
                # find inorder successor (min in right subtree)
                successor = root.right
                while successor.left:
                    successor = successor.left
                # copy successor's data
                root.key, root.val = successor.key, successor.val
                # delete successor
                root.right = self.remove_helper(successor.key, root.right)   
        return root
        
    def getInorderKeys(self) -> List[int]:
        return self.inorderhelper(self.root)
           
    def inorderhelper(self,root):
        if not root:
            return []
        return self.inorderhelper(root.left) + [root.key] + self.inorderhelper(root.right)





