class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        # prefix = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     prefix[i][i] = arr[i]
        #     for j in range(i+1,n):
        #         prefix[i][j]^=prefix[i][j-1]^arr[j]
        #     prefix[i]=prefix[i][i:]
        # # print(prefix)
        ans=[]
        # for [x,y] in queries:
        #         ans.append(prefix[x][y-x])
        # return ans
        for x in range(1,n):
            arr[x]^=arr[x-1]
        for i,j in queries:
            if i==0:
                ans.append(arr[j])
            else:
                ans.append(arr[i-1]^arr[j])
        return ans
