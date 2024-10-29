class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def dfs(r, c):
            max_moves = 0
            
            for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    max_moves = max(max_moves, dfs(nr, nc) + 1)
                    
            return max_moves
        
        result = 0
        for row in range(m):
            result = max(result, dfs(row, 0))
        
        return result
