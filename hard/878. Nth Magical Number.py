class Solution:
    def gcd(self,x,y):
        return x if not y else self.gcd(y,x%y)
    def intersection(self,a,b,lcm,num):
        return num//a+num//b-num//lcm
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        if n==1:
            return min(a,b)
        lcm=a*b//self.gcd(a,b)
        s=min(a,b)
        e=max(a,b)*n
        ans=-1
        while s<=e:      
            m=(s+e)//2
            check=self.intersection(a,b,lcm,m)
            if check==n:
                ans=m
                break
            elif check<n:
                s=m+1
            else:
                e=m-1
        return int(ans%(1e9+7))
# 4 6
# 3
# lcm=12
# 4 6 8
