class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's voting algo
        # candidate = nums[0]
        # freq = 0
        # for i in nums:
        #     if freq == 0:
        #         candidate = i
        #     freq += (1 if candidate == i else -1)
        # count = sum(1 for num in nums if num == candidate)
        # if count > len(nums) // 2:
        #     return candidate
        # else:
        #     return None
        return sorted(nums)[len(nums)//2] #if majority ele is guaranteed
