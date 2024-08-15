class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-10000
        sum=0
        for num in nums:
            sum+=num
            ans=max(ans,sum)
            if sum<0:
                sum=0
        return ans
