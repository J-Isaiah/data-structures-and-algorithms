class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = 0
        new_string = ''

        for i in range(len(word1)):
            new_string += word1[i]

            if word2[r]:
                new_string += word2[r]

            r +=1
        if r+1 != len(word2):
            new_string += word2[r:]

        return new_string

            
        
        