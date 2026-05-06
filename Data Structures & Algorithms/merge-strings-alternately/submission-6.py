class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = 0
        new_string = ''

        for i in range(len(word1)):
            if r >= len(word2):
                new_string += word1[i:]
                break

            new_string += word1[i]
            new_string += word2[r]

            r +=1
        if r <= len(word1):
            new_string += word2[r:]

        return new_string

            
        
        