class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        move=[[1,0],[0,1],[-1,0],[0,-1]]
        dq=deque()
        islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    islands+=1
                    dq.append((i,j))
                while dq:
                    x,y=dq.popleft()
                    grid[x][y]="0"
                    for dx,dy in move:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny]=='1':
                            dq.append((nx,ny))
                            grid[nx][ny]='0'
        return islands
