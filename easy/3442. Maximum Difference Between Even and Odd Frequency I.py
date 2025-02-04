class Solution:
    def maxDifference(self, s: str) -> int:
        e=[]
        o=[]
        for v in Counter(s).values():
            if v%2:
                heapq.heappush(o,-v)
            else:
                heapq.heappush(e,v)
        return -heapq.heappop(o)-heapq.heappop(e)
