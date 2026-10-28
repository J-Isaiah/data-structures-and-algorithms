class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        s = set()
        min = float("inf")
        max = float("-inf")

        for i in nums:
            if i > max:
                max = i

            if i < min:
                min = i

            if i in s:
                return False

            s.add(i)

        return max - min == len(nums) - 1 





