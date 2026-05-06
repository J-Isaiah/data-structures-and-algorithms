class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        buckets = [0,0,0]

        for num in nums:
            buckets[num] += 1
        port = 0 
        for i in range(len(buckets)):
            for n in range(buckets[i]):
                nums[port] = i
                port +=1
                






        