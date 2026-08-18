class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def search(i):
            if i >= len(nums):
                return 0 
            if i in cache:
                return cache[i]
            calc = max(nums[i] + search(i+2), search(i+1))
            cache[i]= calc
            return calc
        return search(0)
        
        