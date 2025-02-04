class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        n = len(grid)
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = defaultdict(int)
        stk = []
        id = 2

        def connect(x, y):
            hash = set()
            temp=1
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] not in hash:
                    temp += islands[grid[nx][ny]]
                    hash.add(grid[nx][ny])
            return temp

        def dfs(x, y, id):
            nonlocal maxSize
            if not (0 <= x < n and 0 <= y < n) or grid[x][y] != 1:
                return 0
            
            grid[x][y] = id
            chunk = 1
            for dx, dy in move:
                chunk += dfs(x + dx, y + dy, id)
            
            maxSize = max(maxSize, chunk)
            return chunk
        
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    islands[id] = dfs(x, y, id)
                    id += 1
                elif grid[x][y] == 0:
                    stk.append((x, y))
        
        while stk:
            maxSize = max(maxSize, connect(*stk.pop()))

        return maxSize
