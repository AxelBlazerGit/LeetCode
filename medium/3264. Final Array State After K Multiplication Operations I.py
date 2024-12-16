class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        for i,n in enumerate(nums):
            heapq.heappush(heap,[n,i])
        while k:
            k-=1
            n,i=heapq.heappop(heap)
            nums[i]*=multiplier
            heapq.heappush(heap,[nums[i],i])
        return nums
