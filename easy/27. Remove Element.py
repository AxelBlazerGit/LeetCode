class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valids=[x for x in nums if x!=val]
        for i in range(len(valids)):
            nums[i]=valids[i]
        return len(valids)
