class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        while s<e:
            mid=(s+e)//2
            if nums[mid]==target:    return mid
            elif nums[mid]>target:   e=mid
            else:   s=mid+1
        return e if nums[e]>=target else e+1
# 1 3 5 6 : 7
# s=0 e=3 m=1
