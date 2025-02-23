class Solution:
    def topK(self,arr,k):
        if not k:   return []
        heap=[]
        for i in range(k):
            heapq.heappush(heap,arr[i])
        for i in range(k,len(arr)):
            if arr[i]>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,arr[i])
        return heap
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap=[]
        for row,lim in zip(grid,limits):
            if lim:
                temp = self.topK(row,lim)
                for n in temp:
                    heapq.heappush(heap, n)
                    if len(heap) > k:
                        heapq.heappop(heap)
        return sum(heap)
