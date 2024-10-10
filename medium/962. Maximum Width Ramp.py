class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        leaders = [None]*n
        cur=n-1
        mx=0
        for i in nums[::-1]:
            leaders[cur]=max(i,mx)
            mx=leaders[cur]
            cur-=1
        ans = 0
        cur = 0

        for i in range(len(leaders)):
            while cur < n and nums[cur] > leaders[i]:
                cur += 1
            ans = max(ans,i-cur)
        return ans
