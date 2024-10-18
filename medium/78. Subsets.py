class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs=[]
        temp=[]
        def bt(idx):
            if idx==len(nums):
                subs.append(temp[:])
                return
            temp.append(nums[idx])
            bt(idx+1)
            temp.pop()
            bt(idx+1)
        bt(0)
        return subs
