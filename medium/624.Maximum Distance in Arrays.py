class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn,mx=arrays[0][0],arrays[0][-1]
        # idxmn,idxmx=-1,-1
        ans=0
        for i in range(1,len(arrays)):
            ans=max(ans,abs(arrays[i][-1]-mn),abs(mx-arrays[i][0]))
            mn=min(arrays[i][0],mn)
            mx=max(arrays[i][-1],mx)
        return ans
