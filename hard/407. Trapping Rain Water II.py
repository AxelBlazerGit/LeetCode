class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m,n=len(heightMap),len(heightMap[0])
        heap=[]
        move=[[1,0],[-1,0],[0,1],[0,-1]]

        for col in range(n):
            if heightMap[0][col]!=-1:
                heappush(heap,(heightMap[0][col],0,col))
            if heightMap[m-1][col]!=-1:
                heappush(heap,(heightMap[m - 1][col],m-1,col))
            heightMap[0][col]=-1
            heightMap[m-1][col]=-1

        for row in range(1, m - 1):
            if heightMap[row][0]!=-1:
                heappush(heap,(heightMap[row][0],row,0))
            if heightMap[row][n-1]!=-1:
                heappush(heap,(heightMap[row][n - 1],row,n-1))
            heightMap[row][0]=-1
            heightMap[row][n-1]=-1
        
        total=0
        hmax=-1

        while heap:
            h,x,y=heappop(heap)
            hmax=max(hmax,h)
            total+=hmax-h

            for dx,dy in move:
                nx,ny=x+dx,y+dy

                if 0<=nx<m and 0<=ny<n and heightMap[nx][ny]!=-1:
                    heappush(heap,(heightMap[nx][ny],nx,ny))
                    heightMap[nx][ny]=-1
            
        return total
