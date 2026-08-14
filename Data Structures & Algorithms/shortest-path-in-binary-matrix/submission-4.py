class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        q.append((0, 0))
        seen.add((0, 0))
        length = 1
        direction = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]

        while q:
            for l in range(len(q)):
                r, c = q.popleft()
                if (r == ROWS - 1) and c == COLS - 1:
                    return length
                for rd, cd in direction:
                    if (
                        (r + rd >= ROWS)
                        or (c + cd >= COLS)
                        or min(r + rd, c + cd) < 0
                        or grid[r + rd][c + cd] == 1
                        or (r + rd,c + cd) in seen
                    ):
                        continue

                    q.append((r + rd, c + cd))
                    seen.add((r + rd, c + cd))
            length += 1
        return length
