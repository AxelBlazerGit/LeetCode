class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax=gmin=nums[0]
        curpos=curneg=total=0
        for i in nums:
            curpos=max(curpos+i,i)
            curneg=min(curneg+i,i)
            gmax=max(gmax,curpos)
            gmin=min(gmin,curneg)
            total+=i
        return max(gmax,total-gmin) if gmax>0 else gmax
