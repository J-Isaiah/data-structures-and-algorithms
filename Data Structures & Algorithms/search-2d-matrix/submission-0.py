class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)-1
        left = 0
        right = rows
        middle = (left+right) //2
        main_matrix = None

        while left <= right:
            print(matrix[middle])
            if target < matrix[middle][0]:
                print(right)
                right = middle - 1
                print('updating right pointer',right)
            elif target >= matrix[middle][0] and target > matrix[middle][-1]:
                left = middle + 1
            elif target >= matrix[middle][0] and target <= matrix[middle][-1]:
                main_matrix = matrix[middle]
                print('target in range breaking loop')
                break
            else:
                return False
            middle = (left+right)//2

        if not main_matrix:
            return False
        
        l = 0 
        r = len(main_matrix) -1
        m = 0

        while l <= r:
            m = (l+r) // 2

            if main_matrix[m]==target:
                return True
            if target > main_matrix[m]:
                l = m +1
            elif target < main_matrix[m]:
                r=m-1

        if main_matrix[l] ==target:
            return True
        return False

                