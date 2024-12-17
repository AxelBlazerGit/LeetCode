class Solution:
    def arrangeCoins(self, n: int) -> int:
        s=0
        e=n
        while s<=e:
            m=(s+e)//2
            if n>=m*(m+1)//2:
                s=m+1
            else:
                e=m-1
        return e
