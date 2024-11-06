class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n==k:    return nums
        final=nums[:k]
        heap=final[:]
        heapq.heapify(heap)
        for i in range(k,n):
            if heap[0]<nums[i]:
                final.remove(heapq.heappop(heap))
                final.append(nums[i])
                heapq.heappush(heap,nums[i])
        return final
