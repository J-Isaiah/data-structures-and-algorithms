class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total = 0
        cur = 0
        for i in range(nums):
            total += i
            cur += nums[1]

        return total - cur
        