class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        arr.extend(nums)
        arr.extend(nums)
        return arr
        