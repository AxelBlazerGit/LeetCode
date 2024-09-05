class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        plusve,minusve=0,1
        new=[0]*len(nums)
        for i in nums:
            if i>0:
                new[plusve]=i
                plusve+=2
            else:
                new[minusve]=i
                minusve+=2
        return new
