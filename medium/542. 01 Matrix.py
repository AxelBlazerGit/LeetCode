class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 01 ms bfs
        m,n=len(isWater),len(isWater[0])
        dq=deque()
        new=[[-1]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if not isWater[i][j]:
                    dq.append((i,j))
                    new[i][j]=0
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while dq:
            x,y=dq.popleft()
            for dx,dy in move:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and new[nx][ny]==-1:
                    dq.append((nx,ny))
                    new[nx][ny]=new[x][y]+1
        return new
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        return self.highestPeak(mat)
