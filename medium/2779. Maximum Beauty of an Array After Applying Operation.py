class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxbeauty=1
        prev=0
        for i in range(1,len(nums)):
            while nums[i]-nums[prev]>2*k:
                prev+=1
            maxbeauty=max(maxbeauty,i-prev+1)
        return maxbeauty
