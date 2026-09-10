class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total = 0
        cur = 0
        for i in range(len(nums)):
            total += i
            cur += nums[i]

        return total - cur
        