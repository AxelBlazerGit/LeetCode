class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 and grid[1][0]>1:    return -1
        m,n=len(grid),len(grid[0])
        times=[(0,0,0)] # time, i, j
        move=[[1,0],[-1,0],[0,1],[0,-1]]
        hash=set(([0,0]))

        while times:
            cur,r,c=heapq.heappop(times)
            if r==m-1 and c==n-1:
                return cur
            for dx,dy in move:
                tx,ty=r+dx,c+dy
                if not (0 <= tx < m and 0 <= ty < n) or (tx, ty) in hash:
                    continue
                nextTime = max(grid[tx][ty] + (0 if abs(grid[tx][ty] - cur) & 1 else 1), cur + 1)
                heapq.heappush(times,(nextTime,tx,ty))
                hash.add((tx,ty))
