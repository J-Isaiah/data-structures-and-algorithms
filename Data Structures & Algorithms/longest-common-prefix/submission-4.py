class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""


        for i in range(len(strs[0])):

            for c in strs:
                if c[i] != strs[0][i]:
                    return pre
            pre += strs[0][i]

        return pre
        