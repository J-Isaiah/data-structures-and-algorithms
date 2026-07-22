import math
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} 

        if k == 0:
            return False
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
                
            if abs(seen[nums[i]]-i) == k:
                return True

        return False
            

            

