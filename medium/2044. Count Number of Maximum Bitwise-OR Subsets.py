class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr=0
        n=len(nums)
        if n==1:    return 1
        for i in nums:  maxOr|=i
        def bt(idx,cur):
            if idx==n:  return 1 if cur==maxOr else 0
            take=bt(idx+1,cur|nums[idx])
            leave=bt(idx+1,cur)
            return take+leave
        return bt(0,0)
