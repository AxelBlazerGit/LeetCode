class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        move=[[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]:
                cur=grid[i][j]
                grid[i][j]=0
                for dx,dy in move:
                    cur+=dfs(i+dx,j+dy)
                return cur
            return 0
        m,n=len(grid),len(grid[0])
        fish=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    fish=max(fish,dfs(i,j))

        return fish
