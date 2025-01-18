class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        move=[None,(0,1),(0,-1),(1,0),(-1,0)]
        m,n=len(grid),len(grid[0])
        dq=deque()
        dq.append([0,0,0])
        hash=defaultdict(lambda: float('inf'))
        hash[(0,0)]=0

        while dq:
            x,y,cost=dq.popleft()
            if (x,y)==(m-1,n-1):
                return cost

            for dir in range(1,5):
                dx,dy=move[dir]
                nx,ny=x+dx,y+dy
                ncost=cost if grid[x][y]==dir else cost+1

                if (nx>=0 and nx<m) and (ny>=0 and ny<n) and (ncost<hash[(nx,ny)]):
                    hash[(nx,ny)]=ncost
                    if dir==grid[x][y]:
                        dq.appendleft((nx,ny,ncost))
                    else:
                        dq.append((nx,ny,ncost))
