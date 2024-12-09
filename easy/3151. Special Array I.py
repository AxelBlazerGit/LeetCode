class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2: return True
        for idx in range(1,len(nums)):
            if (nums[idx]&1) == (nums[idx-1]&1):
                return False
        return True
