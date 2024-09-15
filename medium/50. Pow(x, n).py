class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        ans=self.myPow(x,n//2)
        if n%2:
            ans*=ans*x
        else:
            ans*=ans
        return ans
