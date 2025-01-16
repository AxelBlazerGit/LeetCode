class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 % 2 == 0 and n2 % 2 == 0:
            return 0
        
        ans = 0
        
        if n2 % 2 != 0:
            for num in nums1:
                ans ^= num
        
        if n1 % 2 != 0:
            for num in nums2:
                ans ^= num
        return ans
