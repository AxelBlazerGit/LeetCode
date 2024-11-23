class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u=1
        for i in range(2,len(nums)):
            if nums[i] != nums[u - 1]:
                u += 1
                nums[u] = nums[i]
        return u+1
