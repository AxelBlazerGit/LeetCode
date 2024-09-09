class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral=[[0]*n for _ in range(n)]
        curr=1
        sq=n*n
        top,bottom=0,n
        left,right=0,n
        while curr<sq and top<bottom and left<right:
            # left to right
            for i in range(left,right):
                if curr<=sq:
                    spiral[top][i]=curr
                    curr+=1
                else:
                    return spiral
            top+=1
            # top to bottom
            for i in range(top,bottom):
                if curr<=sq:
                    spiral[i][right-1]=curr
                    curr+=1
                else:
                    return spiral
            right-=1
            # right to left
            for i in range(right-1,left-1,-1):
                if curr<=sq:
                    spiral[bottom-1][i]=curr
                    curr+=1
                else:
                    return spiral
            bottom-=1
            # bottom to top
            for i in range(bottom-1,top-1,-1):
                if curr<=sq:
                    spiral[i][left]=curr
                    curr+=1
                else:
                    return spiral
            left+=1
        if n%2:
            spiral[n//2][n//2]=sq
        return spiral
