class Solution:
    def findScore(self, nums: List[int]) -> int:
        hash=[[ele,idx] for idx,ele in enumerate(nums)]
        heapq.heapify(hash)
        score=0
        marked = [0] * len(nums) # 0 is unmarked 1 is marked
        while hash:
            ele,idx=heapq.heappop(hash)
            if marked[idx]:
                continue
            score+=ele
            marked[idx] = 1
            if idx - 1 >= 0:
                marked[idx - 1] = 1
            if idx + 1 < len(nums):
                marked[idx + 1] = 1
        return score
