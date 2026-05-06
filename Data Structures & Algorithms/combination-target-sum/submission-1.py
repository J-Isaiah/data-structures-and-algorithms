class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        cur = []

        def dfs(ctgt, r):
            
            if ctgt > target:
                return 
            if ctgt == target: 
                if cur not in path:
                
                    path.append(cur.copy())
                return
            
            for i in range(r,len(nums)):
                csum = nums[i] + ctgt
                
                if  csum <= target:
                    cur.append(nums[i])
                    dfs(csum, i)
                    cur.pop()

        dfs(0, 0)

        return path
                
                

                

        