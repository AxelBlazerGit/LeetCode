class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        m,n=len(matrix),len(matrix[0])
        top,bottom=0,m
        left,right=0,n
        cnt=0
        while left<=right and top<=bottom:
            for i in range(left,right):
                if cnt<m*n:
                    ans.append(matrix[top][i])
                    cnt+=1
                else:
                    break
            top+=1
            for i in range(top,bottom):
                if cnt<m*n:
                    ans.append(matrix[i][right-1])
                    cnt+=1
                else:
                    break
            right-=1
            for i in range(right-1,left-1,-1):
                if cnt<m*n:
                    ans.append(matrix[bottom-1][i])
                    cnt+=1
                else:
                    break
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                if cnt<m*n:
                    ans.append(matrix[i][left])
                    cnt+=1
                else:
                    break
            left+=1
        return ans
            
