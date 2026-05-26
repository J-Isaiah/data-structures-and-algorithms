class Solution:
    def mySqrt(self, x: int) -> int:
        left,right  = 0, x
        last_right = 0
        answer = 0

        while left <= right:
            mid =( right + left) //2
            if mid*mid > x:
                right = mid-1

            elif mid*mid <x:
                answer = mid
                left = mid+1
            else:
                answer = mid
                break

        return answer

        