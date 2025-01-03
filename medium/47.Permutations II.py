class Solution:
    ans=[]
    def getPermutations(self,idx,nums):
        if idx==len(nums):
            self.ans.append(nums[:])
            return
        hash=set()
        for i in range(idx,len(nums)):
            if nums[i] in hash:
                continue
            hash.add(nums[i])
            nums[idx],nums[i]=nums[i],nums[idx]
            self.getPermutations(idx+1,nums)
            nums[idx],nums[i]=nums[i],nums[idx]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans.clear()
        self.getPermutations(0,nums)
        return self.ans
        
# net time is factorial complexity
# swap n backtrack..
# swap with front idx and permute
# backtrack when permute of the current over
# base case when all ele exhausted
# class Solution:
#     ans=[]
#     def getPermutations(self,idx,nums):
#         if idx==len(nums):
#             self.ans.append(nums[:])
#             return
#         for i in range(idx,len(nums)):
#             nums[idx],nums[i]=nums[i],nums[idx]
#             self.getPermutations(idx+1,nums)
#             nums[idx],nums[i]=nums[i],nums[idx]

#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.ans.clear()
#         self.getPermutations(0,nums)
#         return self.ans
