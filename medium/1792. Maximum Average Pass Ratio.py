class Solution:
    def delta(self, x, y):
        return (x + 1) / (y + 1) - x / y

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for x, y in classes:
            heapq.heappush(heap, [-self.delta(x, y), x, y])

        while extraStudents > 0:
            d, x, y = heapq.heappop(heap)
            heapq.heappush(heap, [-self.delta(x + 1, y + 1), x + 1, y + 1])
            extraStudents -= 1

        passRatio = 0.0
        for _, x, y in heap:
            passRatio += x / y

        return passRatio / len(classes)
