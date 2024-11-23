class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u=0 # unique
        for i in range(1,len(nums)):
            if nums[i]!=nums[u]:
                nums[i],nums[u+1]=nums[u+1],nums[i]
                u+=1
        return u+1
