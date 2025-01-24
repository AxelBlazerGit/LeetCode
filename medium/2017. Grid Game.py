class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # bot1 creates partition at i
        # bot2 must take max of remaining top or starting bottom
        # bot2's score to be minimized
        # initially : no partition=> idx=-1=> bot2 can choose top row entirely
        top = sum(grid[0])
        bottom = 0
        ans = float('inf')
        
        for i in range(len(grid[0])):
            top -= grid[0][i]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][i]
        
        return ans
