class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n,m=len(matrix),len(matrix[0])
        hash=[None]*m
        for j in range(m):
            temp=-1
            for i in range(n):
                temp=max(temp,matrix[i][j])
            hash[j]=temp
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=hash[j]
        return matrix
