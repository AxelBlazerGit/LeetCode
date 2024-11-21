class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls = set(map(tuple, walls))
        guards = set(map(tuple, guards))
        cell = [[0] * n for _ in range(m)]
        for i, j in guards:
            cell[i][j] = 2  # guard
        for i, j in walls:
            cell[i][j] = -1  # wall
        move=[[-1,0],[1,0],[0,-1],[0,1]] # w s a d
        for gi, gj in guards:
            for dx, dy in move:
                ni, nj = gi + dx, gj + dy
                while 0 <= ni < m and 0 <= nj < n:
                    if cell[ni][nj] == -1 or cell[ni][nj] == 2:
                        break  # wall
                    if cell[ni][nj] == 0:
                        cell[ni][nj] = 1  # flag
                    ni += dx
                    nj += dy
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if cell[i][j] == 0:
                    unguarded += 1
        
        return unguarded
