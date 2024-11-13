class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def lb(l, r, x):
            left, right = l, r
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def ub(l, r, x):
            left, right = l, r
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= x:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        nums.sort()
        fairs = 0

        for i in range(len(nums)):
            l = lb(i + 1, len(nums) - 1, lower - nums[i])
            r = ub(i + 1, len(nums) - 1, upper - nums[i])
            
            if l <= r:
                fairs += r - l + 1
        
        return fairs
