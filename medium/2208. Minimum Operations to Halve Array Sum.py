class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half=sum(nums)/2
        cur=steps=0
        nums=[-x for x in nums]
        heapq.heapify(nums)
        while True:
            temp=-heapq.heappop(nums)
            cur+=temp/2
            steps+=1
            if cur>=half:
                return steps
            heapq.heappush(nums,-temp/2)
        return steps
# 19 8 5 1=> sum=33 at least half is 16.5
# choose 19=>9.5
# 9.5 8 5 1
# choose 9.5=>4.75 , sum = 9.5+4.75 = 14.25
# 8 5 4.75 1
# choose 8=>4, sum = 14.25+4 = 18.25 done
