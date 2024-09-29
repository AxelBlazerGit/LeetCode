class Solution:
    def getSum(self, a: int, b: int) -> int:
        intMax=0xffffffff
        while intMax&b>0:
            a,b=a^b,(a&b)<<1
        return intMax&a if b>0 else a

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         if not min(a,b):
#             return max(a,b)
#         if not max(a,b):
#             return min(a,b)
#         msk=2**32-1
#         while b:
#             a,b=a^b,(a&b)<<1
#         return a&msk if b>0 else a
