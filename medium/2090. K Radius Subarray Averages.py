class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages=[-1]*len(nums)
        if len(nums)<2*k+1:
            return averages
        cur=0
        div=2*k+1
        for i in range(div):
            cur+=nums[i]
        averages[k]=cur//div
        idx=k+1
        for i in range(div,len(nums)):
            cur-=nums[i-div]
            cur+=nums[i]
            averages[idx]=cur//div
            idx+=1
        return averages
