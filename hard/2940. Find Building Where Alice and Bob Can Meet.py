class Solution:
    def minmax(self,it):
        min = max = None
        for val in it:
            if min is None or val < min:
                min = val
            if max is None or val > max:
                max = val
        return min, max

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        hash = defaultdict(list)
        meetups = [-1] * len(queries)

        for idx, (l, r) in enumerate(queries):
            l, r = self.minmax([l, r])
            if l == r or heights[l] < heights[r]:
                meetups[idx] = r
                continue
            hash[r].append([max(heights[l], heights[r]), idx])

        heap = []
        for idx, height in enumerate(heights):
            for h, i in hash[idx]:
                heapq.heappush(heap, [h, i])
            while heap and heap[0][0] < height:
                _, i = heapq.heappop(heap)
                meetups[i] = idx

        return meetups
