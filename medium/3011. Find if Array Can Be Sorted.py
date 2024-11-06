class Solution:
    def bitset(self,n):
        return bin(n).count("1")
    def canSortArray(self, nums: List[int]) -> bool:
        if nums==sorted(nums):  return True
        cur=nums[0]
        prev=0
        bit=self.bitset(nums[0])
        for i in range(1,len(nums)):
            if bit!=self.bitset(nums[i]):
                prev=cur
            if nums[i]>cur:
                cur=nums[i]
                bit=self.bitset(nums[i])
            if nums[i]<prev:
                return False
        return True
