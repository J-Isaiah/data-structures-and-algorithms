class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_diff =float("inf") 
        nums.sort()
        right, left=k, 0
        while left + right -1 <len(nums):


            diff=abs(nums[right+left -1] - nums[left])
            min_diff=min(diff, min_diff)
            left +=1
        
        return min_diff







        