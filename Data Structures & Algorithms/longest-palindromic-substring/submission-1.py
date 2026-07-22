class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):

            right, left= i,i
            while left >= 0 and right < len(s):
                
                if s[left] != s[right]:
                    break

                
                if left+1 <= len(s) and len(s[left:right+1]) > len(result):
                    result = s[left:right+1]
                left-=1
                right+= 1

            right, left= i+1,i
            while left >= 0 and right < len(s)-1:
                
                if s[left] != s[right]:
                    break

                
                if left+1 <= len(s) and len(s[left:right+1]) > len(result):
                    result = s[left:right+1]
                left-=1
                right+= 1
        
        return result 