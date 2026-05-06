class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis= set()
        islands = 0
        col = len(grid[0])
        row = len(grid)
        for r in range(row):
            for c in range(col):
                if (r,c) in vis:
                    continue
                if grid[r][c] == "1":
                    islands += 1
                    self.dfs(vis,grid,r,c,row,col)
        return islands



        
    def dfs(self,vis,grid,r,c, row, col):
        # OOB Case
     
        if (r > row - 1  or c > col - 1) or (c < 0 or r < 0) or (grid[r][c] == '0') or ((r,c) in vis):
            return 0 
        else:
            vis.add((r,c))
        
        self.dfs(vis,grid,r-1,c,row,col)
        self.dfs(vis,grid,r,c-1,row,col)
        self.dfs(vis,grid,r+1,c,row,col)
        self.dfs(vis,grid,r,c+1,row,col)

        

