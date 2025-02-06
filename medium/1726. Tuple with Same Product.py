class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hash=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                hash[nums[i]*nums[j]]+=1
        return 8*sum(x*(x-1)//2 for x in hash.values())
