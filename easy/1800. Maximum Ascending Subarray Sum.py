class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur=mas=nums[0]
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                cur+=nums[i+1]
                mas=max(mas,cur)
            else:
                cur=nums[i+1]
        return mas
