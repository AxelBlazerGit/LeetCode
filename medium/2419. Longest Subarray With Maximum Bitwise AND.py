class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # max AND subarray is same as max streak of max in array
        curMax=nums[0]
        streak=0
        tempStreak=0
        for x in nums:
            if x>curMax:
                tempStreak=1
                curMax=x
                streak=0
            elif x==curMax:
                tempStreak+=1
            else:
                tempStreak=0
            streak=max(streak,tempStreak)
        return streak
