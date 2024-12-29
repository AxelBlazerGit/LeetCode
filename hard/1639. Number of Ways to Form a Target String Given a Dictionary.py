class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod=10**9+7
        def makegrid(words):
            n = len(words[0])
            grid = [[0] * 26 for _ in range(n)]
            for word in words:
                for idx, char in enumerate(word):
                    grid[idx][ord(char) - ord('a')] += 1
            return grid
        grid=makegrid(words)

        hash=defaultdict(int)
        def ways(grid, target, idx, k):
            if idx == len(target):
                return 1
            if k == len(grid):
                return 0
            if (idx, k) in hash:
                return hash[(idx, k)]
            
            ch = target[idx]
            if grid[k][ord(ch) - 97]>0:
                take = grid[k][ord(ch) - 97] * ways(grid, target, idx + 1, k + 1)
                leave = ways(grid, target, idx, k + 1)
                hash[(idx, k)] = (take + leave)
            else:
                hash[(idx, k)] = ways(grid, target, idx, k + 1)
            
            return hash[(idx, k)]
        
        return ways(grid, target, 0, 0) % mod
