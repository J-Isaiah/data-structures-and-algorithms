class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def search(r,c, ROWS, COLS):
            if r > ROWS or c > COLS:
                return 0

            if (r,c) == (ROWS-1, COLS-1):
                return 1

            return (search(r+1,c, ROWS, COLS) + search(r,c+1,ROWS,COLS))
        
        return search(0,0,m,n)