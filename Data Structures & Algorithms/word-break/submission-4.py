class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        c = {}
        def dp(idx):
            if idx in c:
                return c[idx]
            if idx == len(s):
                return True

            for word in wordDict:
                if s[idx : idx + len(word)] == word:
                    branch = dp(idx + len(word))
                    if not branch:
                        c[idx]=False
                        continue 
                    
                    c[idx]=True

                    return True


                        
            
            return False
        
        return dp(0)
                    

        