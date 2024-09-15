class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        ans=self.myPow(x,n//2)%1337
        ans=(ans*ans)%1337
        if n%2:
            ans=(ans*x)%1337
        return ans
    def superPow(self, a: int, b: List[int]) -> int:
        return int(self.myPow(a,int(''.join(map(str,b)))))%1337
        
