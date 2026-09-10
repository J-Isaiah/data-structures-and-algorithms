class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = 0

        for num in nums:
            if num != cur:
                return cur
            cur += 1

        return 0
        