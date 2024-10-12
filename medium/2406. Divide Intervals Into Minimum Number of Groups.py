class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        st=sorted([i[0] for i in intervals])
        ed=sorted([i[1] for i in intervals])
        ans=0
        l=r=0
        while l<len(st):
            if st[l]<=ed[r]:
                l+=1
            else:
                r+=1
            ans=max(ans,abs(r-l))
        return ans
