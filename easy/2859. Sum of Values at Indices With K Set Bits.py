class Solution:
    # leetcode : Counting Bits
    def countBits(self, n: int) -> List[int]:
        bits=[0]*(n+1)
        power=1 # reset at powers of 2
        for i in range(1,n+1):
            if power==i//2:
                power=i
            bits[i]=1+bits[i-power] # number of bits in bin(x)=1+bits in bin(x-lastPowerOf2)
        return bits

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n=len(nums)
        hash=self.countBits(n)
        kSetBits=0
        for idx,bits in enumerate(hash):
            if idx==n:
                break
            if bits==k:
                kSetBits+=nums[idx]
        return kSetBits
