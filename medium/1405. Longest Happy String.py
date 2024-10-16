class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # While heap:
        #     Pop most frequent ch from heap.
        #     If adding current ch creates 3 consecutive identical:
        #         Pop second most frequent ch, add to result, update count.
        #         Push original most frequent ch into heap.
        #     Else: append most frequent ch to result and update count.
        heap = [(-x, ch) for x, ch in [(a, 'a'), (b, 'b'), (c, 'c')] if x]
        heapq.heapify(heap)
        result = []
        while heap:
            c1, ch1 = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == ch1 and result[-2] == ch1:
                if not heap:
                    break
                c2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                c2 += 1
                if c2:
                    heapq.heappush(heap, (c2, ch2))
                heapq.heappush(heap, (c1, ch1))
            else:
                result.append(ch1)
                c1 += 1
                if c1:
                    heapq.heappush(heap, (c1, ch1))
        return ''.join(result)
