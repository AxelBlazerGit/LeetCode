class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        rem=sum(nums)
        cur=splits=0
        for i in nums[:-1]:
            cur+=i
            rem-=i
            if cur>=rem:
                splits+=1
        return splits
