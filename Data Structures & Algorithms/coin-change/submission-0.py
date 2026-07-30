class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = set()
        q = collections.deque([amount])
        coins_used = 0
        while q: 
            level_size = len(q)
            coins_used += 1
            for l in range(level_size):
                cur_amount = q.popleft()
                for coin in coins:
                    remainder = cur_amount - coin
                    
                    if remainder > 0:
                        q.append(remainder)
                    if remainder == 0:
                        return coins_used
                        
        
        return -1
                

            
