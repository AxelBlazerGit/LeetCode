class Solution:
    def parity(self,x):
        parity=0
        for i in str(x):
            if i in "13579":
                parity=(parity+1)%2
        return parity
    def countEven(self, num: int) -> int:
        ans=0
        for i in range(2,num+1):
            ans+=1 if not self.parity(i) else 0
        return ans
