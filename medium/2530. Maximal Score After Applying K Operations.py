class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        heapq.heapify(nums)
        score=0
        while k:
            temp=-heapq.heappop(nums)
            score+=temp
            temp=temp//3 if temp//3==temp/3 else (temp//3+1)
            heapq.heappush(nums,-temp)
            k-=1
        return score
