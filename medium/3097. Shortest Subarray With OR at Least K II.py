class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        streak=2*(10**5)+1
        l=0
        hash=[0]*32
        def bit(idx,move):
            for i in range(32):
                if idx&(1<<i):
                    hash[i]+=move
        def binary():
            streak=0
            for i in range(32):
                if hash[i]:
                    streak+=1<<i
            return streak
        for r in range(len(nums)):
            bit(nums[r],1)
            cur=binary()
            while l<=r and cur>=k:
                streak=min(streak,r-l+1)
                bit(nums[l],-1)
                cur=binary()
                l+=1
            
        return streak if streak!=2*(10**5)+1 else -1
