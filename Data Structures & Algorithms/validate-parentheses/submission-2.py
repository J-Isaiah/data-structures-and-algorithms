class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{',']':'['}

        stack = []

        if s[0] in closeToOpen:
            return False   

        for i in range(len(s)):
            if i in closeToOpen:
                top_of_stack = stack[-1]
                print(top_of_stack)
                
                if closeToOpen[i] != top_of_stack:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return True
            

            

            
            
            
        