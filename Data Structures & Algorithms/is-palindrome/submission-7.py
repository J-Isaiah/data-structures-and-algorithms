class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = 0
        left = len(s) -1
        s = s.lower()
        while right < left:

            if right >= len(s):
                return False

            while not right>=len(s) and not s[right].isalnum():
                right += 1
            while not s[left].isalnum() and not left <=0:
                left -=1

            if s[right] != s[left]:
                return False

            right +=1
            left -=1

        return True

        