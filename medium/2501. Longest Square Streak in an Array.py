class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = -1
        
        for num in sorted(nums):
            cur = 1
            nxt = num * num
            while nxt in nums:
                cur += 1
                nxt = nxt * nxt
            
            if cur >= 2:
                streak = max(streak, cur)
        return streak if streak!=1 else -1
