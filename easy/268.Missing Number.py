class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s=sum(nums)
        n=len(nums)
        ans=0
        # expected=n*(n+1)//2
        # return expected-s
        for i in range(n):
            ans^=nums[i]^i
        return ans^n
# xor is for bitManipulation method and expected is for mathematical method
