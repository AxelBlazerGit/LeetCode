class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        ans = 0
        for i in range(n):
            for j in range(m):
                min_height = n + 1
                for k in range(j, -1, -1):
                    min_height = min(min_height, matrix[i][k])
                    if min_height < j - k + 1:
                        break
                    ans += 1

        return ans
