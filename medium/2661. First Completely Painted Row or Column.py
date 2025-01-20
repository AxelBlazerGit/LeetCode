class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        hash={}
        for i in range(m):
            for j in range(n):
                hash[mat[i][j]]=[i,j]
        r,c=[n]*m,[m]*n
        for i in range(len(arr)):
            x,y=hash[arr[i]]
            r[x]-=1
            c[y]-=1
            if not r[x] or not c[y]:
                return i
