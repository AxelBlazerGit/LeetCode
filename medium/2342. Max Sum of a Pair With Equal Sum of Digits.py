class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumOfDigits(x):
            s=0
            while x:
                s+=x%10
                x//=10
            return s
        hash=defaultdict(list)
        for n in nums:
            heapq.heappush(hash[sumOfDigits(n)],-n)
        ms=0
        for lst in hash:
            if len(hash[lst])>1:
                x,y=-heapq.heappop(hash[lst]),-heapq.heappop(hash[lst])
                ms=max(ms,x+y)
        return ms if ms else -1
