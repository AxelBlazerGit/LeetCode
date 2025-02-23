class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for s in stones:    heapq.heappush(heap,-s)
        while heap:
            if len(heap)==1:    break
            x,y=-heapq.heappop(heap),-heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,-abs(x-y))
        return -heap[0] if heap else 0
