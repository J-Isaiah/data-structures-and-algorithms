class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        seconds = 1
        seen = set()
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]

                if cell == 2:
                    q.append((r, c))
                    seen.add((r, c))

                elif cell == 1:
                    fresh += 1

        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()

                for dr, dc in directions:
                    nr, nc = cr + dr, dc + cc
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in seen:
                        continue

                    cur_val = grid[nr][nc]

                    if cur_val == 0:
                        continue

                    if cur_val == 1:
                        seen.add((nr, nc))
                        q.append((nr, nc))
                        fresh -= 1

            if fresh == 0:
                return seconds

            seconds += 1
        return -1
