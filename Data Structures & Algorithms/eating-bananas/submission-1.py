import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_int = max(piles)
        l,r,k = 1, max_int,0

        answer = 0

        while l <= r:
            k = (l+r)//2

            total_time = 0
            for i in piles:
                total_time += math.ceil(i/k)
            print(total_time,k)
            
            if total_time <= h:
                answer = (k)
                r = k-1
            elif total_time > h:
                l = k+1
            
        return answer


        