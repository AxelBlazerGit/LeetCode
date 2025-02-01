class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, idx):
            if idx == len(word):
                return True
            if not (0 <= x < m and 0 <= y < n) or (x, y) in hash or board[x][y] != word[idx]:
                return False

            hash.add((x, y))
            for dx, dy in move:
                if dfs(x + dx, y + dy, idx + 1):
                    return True
            hash.remove((x, y))

            return False

        m, n = len(board), len(board[0])
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    hash = set()
                    if dfs(x, y, 0):
                        return True

        return False
