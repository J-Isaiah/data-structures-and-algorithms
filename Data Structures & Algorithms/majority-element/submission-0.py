class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}

        for i in nums:
            elements[i] = elements.get(i, 0) + 1

        return max(elements, key=elements.get)
        