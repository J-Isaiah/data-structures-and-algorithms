class node:
    def __init__(self,val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next=next
class Deque:
    
    def __init__(self):
        self.head = node(-1)
        self.tail = node(-1, prev=self.head)
        self.head.next = self.tail


    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        

    def append(self, value: int) -> None:
        new_node = node(value)
        last_node = self.tail.prev
        
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node
            
        
        

    def appendleft(self, value: int) -> None:
       new_node = node(value)
       first_node = self.head.next

       self.head.next = new_node
       new_node.prev = self.head
       new_node.next = first_node
       first_node.prev = new_node


    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        
        last_node = self.tail.prev
        prev_node = last_node.prev
        prev_node.next =  self.tail
        self.tail.prev = prev_node 
        
        return last_node.val
        
        

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1

        first_node = self.head.next 
        next_node = first_node.next
        self.head.next = next_node
        next_node.prev=self.head

        return first_node.val
        
