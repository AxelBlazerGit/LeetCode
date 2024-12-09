class Solution:
    def minmax(self, arr):
        
        m, M = arr[0], arr[0]

        for num in arr[1:]:
            if num < m:
                m = num
            elif num > M:
                M = num
        
        return m, M

    def countElements(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0

        low,high=self.minmax(nums)
        ele=0
        for i in nums:
            if i>low and i<high:
                ele+=1
        return ele
