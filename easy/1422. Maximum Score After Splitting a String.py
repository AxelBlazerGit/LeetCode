class Solution:
    def maxScore(self, s: str) -> int:
        z,o=0,s.count("1")
        ans=z
        for i in range(len(s)-1):
            if s[i]=='1':
                o-=1
            else:
                z+=1
            ans=max(ans,z+o)
        return ans
