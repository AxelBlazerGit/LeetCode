class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window: linear time
        # right pointer expands the window by including elements from nums.
        # left pointer shrinks the window from the left when the current sum 
        # becomes greater than or equal to the target.
        # for every valid window (sum >= target), the minimal length 
        # is updated by calculating the window size (right - left + 1).
        # left pointer continues to move right to find the smallest possible 
        # subarray that satisfies the condition.
        if sum(nums) < target:
            return 0
        l = temp = 0
        ans = 10**5 + 1
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                ans = min(ans, r - l + 1)
                temp -= nums[l]
                l += 1  # shrink window
        return ans if ans != (10 ** 5 + 1) else 0
