class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        adj=-float('inf')
        for i in range(len(nums)-1):
            adj=max(adj,abs(nums[i]-nums[i+1]))
        return max(adj,abs(nums[0]-nums[-1]))
