class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-x for x in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            temp=-heapq.heappop(gifts)
            heapq.heappush(gifts,-int(sqrt(temp)))
        return -sum(gifts)
# 100 64 25 9 4 k=4
# take 100 leave 10
# 64 25 10 9 4
# take 64 leave 8
# 25 10 9 8 4
# take 25 leave 5
# 10 9 8 5 4
# take 10 leave 3
# 9 8 5 4 3=> sum=29
