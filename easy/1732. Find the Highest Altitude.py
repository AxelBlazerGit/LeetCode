class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        ans=0
        for i in gain:
            curr+=i
            ans=max(ans,curr)
        return ans
