class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        curSum=0

        # o(n )
        for n in nums:
            new = curSum+n
            maxSum = max(maxSum, new)
            curSum = max(0, new)

        return maxSum
        