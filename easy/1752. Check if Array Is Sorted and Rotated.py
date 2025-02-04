class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        ans=1 if nums[-1]>nums[0] else 0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                ans+=1
        return ans<=1
