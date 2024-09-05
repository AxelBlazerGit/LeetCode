class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        ptr=0
        for ele in nums:
            if ele:
                ptr+=1
                ans=max(ans,ptr)
            else:
                ptr=0
        return ans
