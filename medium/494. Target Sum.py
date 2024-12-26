class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curidx=defaultdict(int)
        curidx[0]=1 # idx,choose
        for i in range(len(nums)):
            nextidx=defaultdict(int)
            for k,v in curidx.items():
                nextidx[k+nums[i]]+=v
                nextidx[k-nums[i]]+=v
            curidx=nextidx
        return curidx[target]
