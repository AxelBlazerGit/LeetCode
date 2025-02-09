class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            N=0
            while n:
                N=N*10+n%10
                n//=10
            return N
        if len(nums)<2:
            return 0
        hash=defaultdict(int)
        nice=0
        for i,e in enumerate(nums):
            nice+=hash[e-rev(e)]
            nice%=(10**9+7)
            hash[e-rev(e)]+=1
        return nice%(10**9+7)
