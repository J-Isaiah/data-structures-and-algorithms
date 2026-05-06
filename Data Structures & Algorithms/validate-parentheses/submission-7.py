class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{',']':'['}

        stack = []

        if s[0] in closeToOpen:
            return False   

        for i in s:
            if i in closeToOpen:
                if not stack or closeToOpen[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
            

            

            
            
            
        