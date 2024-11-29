class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque([(0, 0, 0)])  # dist,x,y
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = [[None] * n for _ in range(m)]
        ans[0][0] = 0

        while dq:
            dist, x, y = dq.popleft()
            for dx, dy in move:
                X, Y = x + dx, y + dy
                if 0 <= X < m and 0 <= Y < n and ans[X][Y] is None:
                    if grid[X][Y]:
                        ans[X][Y] = dist + 1
                        dq.append((ans[X][Y], X, Y))
                    else:
                        ans[X][Y] = dist
                        dq.appendleft((dist, X, Y))

        return ans[-1][-1]
