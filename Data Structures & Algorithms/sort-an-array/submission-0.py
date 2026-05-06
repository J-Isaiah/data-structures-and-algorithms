class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums):

            if len(nums) <=1:
                return nums 

            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            
            return merge(left, right)

        def merge(left,right):
            output = []
            if not right and not left:
                return []
            if not right: 
                return left
            if not left:
                return right 

            lp, rp = 0,0

            while lp != len(left) and rp!=len(right):
                if left[lp] >= right[rp]:
                    output.append(right[rp])
                    rp+=1
                else:
                    output.append(left[lp])
                    lp+=1

            if lp < len(left) and rp >= len(right):
                output.extend(left[lp:]) 
            if rp < len(right) and lp >= len(left):
                output.extend(right[rp:])

            return output
        
        return mergeSort(nums)
                
        