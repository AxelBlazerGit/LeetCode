class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash=Counter(nums)
        hash = [(-freq, num) for num, freq in hash.items()]
        heapq.heapify(hash)
        topK=[]
        while k and hash:
            freq, num = heapq.heappop(hash)
            topK.append(num)
            k -= 1
        return topK
