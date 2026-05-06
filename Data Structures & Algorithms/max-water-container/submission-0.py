class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        answer = 0

        for i in range(len(heights)):
            new_vol = (r-l) * min(heights[r], heights[l])

            if new_vol >= answer:
                answer = new_vol

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1

        return answer





        