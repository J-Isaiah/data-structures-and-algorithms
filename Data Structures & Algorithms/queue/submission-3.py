class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        


    def isEmpty(self) -> bool:
        if self.head.next != self.tail:
            return False
        return True
        

    def append(self, value: int) -> None:
       past_node = self.tail.prev
       new_node = Node(value)
       
       past_node.next = new_node
       new_node.next = self.tail
       new_node.prev=past_node
       self.tail.prev = new_node

        

    def appendleft(self, value: int) -> None:
        new = Node(value)

        next_node= self.head.next

        self.head.next = new
        new.prev=self.head
        new.next=next_node

        next_node.prev=new

        

    def pop(self) -> int:
        if self.head.next == self.tail: 
            return -1

        removed_node = self.tail.prev
        prev_node = removed_node.prev

        prev_node.next = self.tail
        self.tail.prev=prev_node

        return removed_node.val


        

        

    def popleft(self) -> int:
        if self.head.next == self.tail: 
            return -1
        
        removed_node = self.head.next
        next_node = removed_node.next

        self.head.next = next_node
        next_node.prev=self.head 


        return removed_node.val

        
        
