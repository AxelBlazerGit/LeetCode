class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        mid = (2**n) // 2
        
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirrored_k = 2**n - k
            return '1' if self.findKthBit(n - 1, mirrored_k) == '0' else '0'
