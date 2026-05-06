class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1], [-1,0],[-1,-1],[-1,1],[1,1],[1,-1]]
        seen = set()
        queue = collections.deque([(0,0)])
        row, col = len(grid), len(grid[0])
        length = 1


        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1

        while queue:

            for _ in range(len(queue)):
                cur_row, cur_col = queue.popleft()
                

                if [cur_row,cur_col] == [row-1,col-1]:
                    return length if length else -1
                for rd, cd in directions:
                    if ((cur_row+rd,cur_col+cd) in seen) or (not (0 <=cur_row + rd < row) or not (0 <=cur_col + cd < col)or grid[cur_row+rd][cur_col+cd]==1):
                        continue
                    queue.append((cur_row+rd, cur_col+cd))
                    seen.add((cur_row+rd,cur_col+cd))
            length +=1

        return -1