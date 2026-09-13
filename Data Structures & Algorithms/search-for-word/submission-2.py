class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        def dfs(row, col, i, path):
            path = set()
            if i >= len(word):
                return True
            if row < 0 or col < 0 or row >= ROW or col >= COL:
                return False

            if board[row][col] != word[i]:
                return False

            if (row, col) in path:
                return False

            path.add((row,col))

            return (
                dfs(row + 1, col, i + 1, path)
                or dfs(row - 1, col, i + 1, path)
                or dfs(row, col + 1, i + 1, path)
                or dfs(row, col - 1, i + 1, path)
            )

        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0, set()):
                    return True
        return False
