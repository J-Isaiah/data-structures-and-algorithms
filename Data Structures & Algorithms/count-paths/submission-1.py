class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def search(r,c, ROWS, COLS, cache):
            if r >= ROWS or c >= COLS:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]

            if (r,c) == (ROWS-1, COLS-1):
                return 1
                
            cache[(r,c)] = (search(r+1,c, ROWS, COLS, cache) + search(r,c+1,ROWS,COLS, cache))
            return cache[(r,c)]
        
        return search(0,0,m,n, {})