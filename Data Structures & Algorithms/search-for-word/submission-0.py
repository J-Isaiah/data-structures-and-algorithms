class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        def dfs(row, col, i):
            if i >= len(word):
                return True
            if ROW < 0 or col < 0 or row >= ROW or col >= COL:
                return False

            if board[row][col] != word[i]:
                return False

            return (
                dfs(row + 1, col, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col + 1, i + 1)
                or dfs(row, col - 1, i + 1)
            )

        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False
