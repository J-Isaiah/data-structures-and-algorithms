class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()
        q.append((0, 0))
        seen.add((0, 0))

        direction = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]

        while q:
            for l in range(len(q)):
                r, c = q.popleft()
                for rd, cd in direction:
                    if (
                        (r + rd >= ROWS)
                        or (c + cd >= COLS)
                        or min(r + rd, c + cd) < 0
                        or grid[r + rd][c + cd] == 1
                        or grid[r + rd][c + cd] in seen
                    ):
                        continue
