class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        start_color = image[sr][sc]

        def dfs(start_color, image, r, c, seen):

            ROW, COL = len(image), len(image[0])

            # check oob or seen
            if r<0 or r >= ROW or c<0 or c >= COL or (r, c) in seen:
                return
            # check same color 
            if image[r][c] != start_color:
                return
            else: 
                image[r][c] = color 

            seen.add((r,c))

            
            

            dfs(start_color, image, r + 1, c, seen)  # right 1
            dfs(start_color, image, r - 1, c, seen)  # left 1
            dfs(start_color, image, r, c + 1, seen)  # down 1
            dfs(start_color, image, r, c - 1, seen)  # up 1

        dfs(start_color, image, sr,sc, seen)
        return image
        
