class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        ans,curr=1,1
        for i in nums:
            if i-1 not in nums:
                curr=1
                while i+curr in nums:
                    curr+=1
                    ans=max(ans,curr)
        return ans
