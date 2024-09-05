class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[[0]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j==0 or j==i:
                    pascal[i][j]=1
                else:
                    pascal[i][j]=pascal[i-1][j]+pascal[i-1][j-1]
        return pascal
