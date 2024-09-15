class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]+=nums[i+1]
                nums[i+1]=0
        def moveZeroes(nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            nonz=0
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i],nums[nonz]=nums[nonz],nums[i]
                    nonz+=1
        moveZeroes(nums)
        return nums
