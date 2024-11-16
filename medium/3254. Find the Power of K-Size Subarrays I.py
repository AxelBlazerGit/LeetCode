class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        power=[]
        l=0
        streak=1
        for r in range(len(nums)):
            if r and nums[r]==nums[r-1]+1:
                streak+=1
            if r-l+1>k:
                if nums[l]==nums[l+1]-1:
                    streak-=1
                l+=1
            if r-l+1==k:
                power.append(nums[r] if streak==k else -1)
        return power
