class Solution:
    def countBits(self, n: int) -> List[int]:
        bits=[0]*(n+1)
        power=1 # reset at powers of 2
        for i in range(1,n+1):
            if power==i//2:
                power=i
            bits[i]=1+bits[i-power] # number of bits in bin(x)=1+bits in bin(x-lastPowerOf2)
        return bits




# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         bits=[0]*(n+1)
#         for i in range(1,n+1):
#             cur=i
#             while cur:
#                 if cur&1:
#                     bits[i]+=1
#                 cur>>=1
#         return bits 
