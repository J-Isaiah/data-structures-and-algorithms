import math
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} 

        if k == 0:
            return False

        for i in range(len(nums)):          
            if seen[nums[i]] is not None and abs(seen[nums[i]]-i) <= k:
                return True
            seen[nums[i]] = i

        return False
            

            

