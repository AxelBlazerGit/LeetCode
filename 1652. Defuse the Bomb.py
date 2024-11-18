class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        defuse=[0]*n
        if not k:   return defuse
        l,r=(1,k) if k>0 else (n+k,n-1)
        cur=0
        for i in range(l,r+1):
            cur+=code[i%n]
        for i in range(n):
            defuse[i] = cur
            cur -= code[(l) % n]
            cur += code[(r + 1) % n]
            l += 1
            r += 1
        return defuse
