class Solution:
    def columns(self,grid):
        m,n=len(grid),len(grid[0])
        flips=0
        for i in range(n):
            l,r=0,m-1
            while l<r:
                if grid[l][i]!=grid[r][i]:
                    flips+=1
                l+=1
                r-=1
        return flips

    def rows(self,grid):
        m,n=len(grid),len(grid[0])
        flips=0
        for i in range(m):
            l,r=0,n-1
            while l<r:
                if grid[i][l]!=grid[i][r]:
                    flips+=1
                l+=1
                r-=1
        return flips
        
    def minFlips(self, grid: List[List[int]]) -> int:
        return min(self.rows(grid),self.columns(grid))
