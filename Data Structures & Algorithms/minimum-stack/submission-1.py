class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.stack[-1] <= self.stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        poped_val = self.stack.pop()

        if poped_val == self.min_stack[-1]:
            self.min_stack.pop()
        

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


        
        
        
