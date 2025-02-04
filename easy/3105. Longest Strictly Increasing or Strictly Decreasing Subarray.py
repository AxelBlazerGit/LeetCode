class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur=lms=1
        for x in range(len(nums)-1):
            if nums[x]<nums[x+1]:
                cur+=1
            else:
                cur=1
            lms=max(lms,cur)
        cur=1
        for x in range(len(nums)-1):
            if nums[x]>nums[x+1]:
                cur+=1
            else:
                cur=1
            lms=max(lms,cur)
        return lms
