class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        hash=defaultdict(int)
        good=0
        for i,e in enumerate(nums):
            good+=hash[e-i]
            hash[e-i]+=1
        return len(nums)*(len(nums)-1)//2-good
