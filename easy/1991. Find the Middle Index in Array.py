class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        cur=0
        for i in range(len(nums)):
            if i:cur+=nums[i-1]
            if s-nums[i]==2*cur:
                return i
        return -1
