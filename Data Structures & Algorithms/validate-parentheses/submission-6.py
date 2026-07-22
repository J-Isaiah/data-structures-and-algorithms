class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{',']':'['}

        stack = []

        if s[0] in closeToOpen:
            return False   

        for i in s:
            if i in closeToOpen:
                top_of_stack = stack[-1]
                print(top_of_stack)
                
                if not stack or closeToOpen[i] != top_of_stack:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
            

            

            
            
            
        