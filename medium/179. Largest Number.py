class Solution:
    def greater(self,x,y):
        # custom sort to find greater integer when combined
        return 1 if x+y<y+x else -1
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums)==set([0]):
            return "0"
        nums=[str(ele) for ele in nums]
        nums=sorted(nums,key=cmp_to_key(self.greater))
        return "".join(nums)
