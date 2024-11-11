#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        moves=0
        cur=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<=cur:
                moves+=cur+1-arr[i]
                cur+=1
            else:
                cur=arr[i]
        return moves
