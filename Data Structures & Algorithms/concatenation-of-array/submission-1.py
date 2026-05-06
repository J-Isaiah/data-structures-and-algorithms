class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        new_array=[]
        new_array.extend(nums)
        for num in nums:
            new_array.append(num)

        return new_array      