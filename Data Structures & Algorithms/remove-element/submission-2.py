class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right, left = 0,len(nums)-1

        while right <= left:
            if nums[left]==val:
                left-=1
                continue
            if nums[right]==val:
                nums[right], nums[left]= nums[left], nums[right]
                right+=1
                left-=1
            else:
                right+=1

        return right

        
        