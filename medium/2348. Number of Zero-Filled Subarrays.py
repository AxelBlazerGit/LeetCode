class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # pseudo: all the subarray count of including zeroes are similar to cumulative zeroes sum
        zeros = 0
        curr = 0
        for i in nums:
            if i == 0:
                curr += 1
                zeros += curr
            else:
                curr = 0
        return zeros
