class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(idx):
            if idx == len(s):
                return True

            for word in wordDict:
                if s[idx : idx + len(word)] == word:
                    branch =dp(idx + len(word))
                    if not branch:
                        continue 

                        
            
            return False
        
        return dp(0)
                    

        