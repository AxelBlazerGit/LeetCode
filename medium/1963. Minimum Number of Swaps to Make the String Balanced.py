class Solution:
    def minSwaps(self, s: str) -> int:
        if not s:
            return 0
        n=len(s)
        open=0
        swap=0
        for i in range(n):
            if s[i]=='[':
                open+=1
            elif open:
                open-=1
            else:
                swap+=1
        return (swap+1)//2
