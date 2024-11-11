class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        while b:
            a,b=a^b,(a&b)<<1
        return bin(a)[2:]
