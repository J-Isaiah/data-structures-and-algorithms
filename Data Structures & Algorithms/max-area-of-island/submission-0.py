class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        seen = set()
        row  = len(grid) 
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and ((r,c) not in seen):
                    largest = max(self.dfs(grid,row,col,r,c,seen), largest)
                
                seen.add((r,c))

        return largest

    def dfs(self, grid, row, col, r,c,seen):
        count = 0


        if r < 0 or c < 0 or r >= row or c >= col:
            return 0


        if grid[r][c] == 0:
            return 0


        if (r, c) in seen:
            return 0

        
        if grid[r][c] == 1:
            count += 1
            seen.add((r,c))

        count += self.dfs(grid,row,col,r-1,c,seen)
        count += self.dfs(grid,row,col,r,c-1,seen)
        count += self.dfs(grid,row,col,r,c+1,seen)
        count += self.dfs(grid,row,col,r+1,c,seen)

        return count






        