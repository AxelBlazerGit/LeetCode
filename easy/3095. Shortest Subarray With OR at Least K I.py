class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=51
        flag=False
        for i in range(len(nums)):
            temp=nums[i]
            for j in range(i,len(nums)):
                temp|=nums[j]
                if temp>=k:
                    flag=True
                    ans=min(ans,j-i+1)
                    break
        return ans if flag else -1
