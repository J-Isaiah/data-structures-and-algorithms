class Solution:
    def rob(self, nums: List[int]) -> int:

        def search(i):
            if i >= len(nums):
                return 0 
            return max(nums[i] + search(i+2), search(i+1))
        return search(0)
        
        