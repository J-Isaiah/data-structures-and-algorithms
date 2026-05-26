class Node():
    def __init__(self, key = None,next=None, prev=None, val=None):
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.h = {}
        self.length=0
        self.most =Node()
        self.least =Node()
        self.most.next = self.least
        self.least.prev = self.most

        

    def get(self, key: int) -> int:
        node = self.h.get(key, None)

        if not node:
            return -1
        
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

        place= self.most.next
        self.most.next=node
        node.next=place
        place.prev=node
        node.prev=self.most

        return node.val
        


        

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.h[key].val = value 
            self.get(key)
            return

            

        new_node = Node(val=value, key= key)
        self.h[key] = new_node
        place = self.most.next
        self.most.next=new_node
        new_node.prev=self.most
        new_node.next=place
        place.prev=new_node

        if len(self.h) > self.cap:
            lru = self.least.prev
            lru.next = None
            del self.h[lru.key]

            prev = lru.prev
            prev.next = self.least
            self.least.prev=prev

        
