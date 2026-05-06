class node:
    def __init__ (self, val, next=None):
        self.val = val
        self.next=next
class LinkedList:
    
    def __init__(self):
        self.tail = node(-1)
        self.head = node(-1, self.tail)
        
        

    
    def get(self, index: int) -> int:
        next_node = self.head.next
        while index != 0 and next_node.next != None:
            next_node = next_node.next
            index -=1

        return next_node.val if next_node else -1


        

    def insertHead(self, val: int) -> None:
        saved_node = self.head.next
        new_node = node(val, saved_node)
        self.head.next = new_node
        

    def insertTail(self, val: int) -> None:
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = node(val, self.tail)
        

    def remove(self, index: int) -> bool:
        prev_node = self.head
        current_node = self.head.next
        
        while current_node != self.tail and index > 0:
            prev_node = current_node
            current_node = current_node.next
            index -= 1

        if current_node == self.tail:
            return False
        
        # Remove the node by linking the previous node to the next node
        prev_node.next = current_node.next
        return True

        
        


        

    def getValues(self) -> List[int]:
        vals = []
        current_node = self.head.next
        while current_node != None and current_node != self.tail:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals
