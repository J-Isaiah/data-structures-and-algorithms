class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        r = len(s)-2
        
        for l in range(len(s)):
            print(s[l],s[r])

            if s[l] != s[r]:
                return False
            
            if r ==l:
                return True
            
            r-=1

            

            
            
        return True

            
        