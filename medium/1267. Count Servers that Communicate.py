class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        rhash,chash=[0]*m,[0]*n
        for i in range(m):
            for j in range(n):
                rhash[i]+=grid[i][j]
                chash[j]+=grid[i][j]
        communicators=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rhash[i] + chash[j])>2:
                    communicators+=1
        return communicators
