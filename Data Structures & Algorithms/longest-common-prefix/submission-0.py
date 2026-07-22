class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        index = 0

        for w in strs:
            char = w[index]
            for j in strs:
                if char != j[index]:
                    return pre
                
            pre += char
            index +=1

                

