class Solution:
    def count(self,n,curr):
        next=curr+1
        ans=0
        while curr<=n:
            if next<=n:
                ans+=next-curr
            else:
                ans+=n-curr+1
            curr*=10
            next*=10
        return ans
    def findKthNumber(self, n: int, k: int) -> int:
        if k==1:
            return 1
        curr=1
        k-=1
        while k:
            steps=self.count(n,curr)
            if steps<=k:
                k-=steps
                curr+=1
            else:
                curr*=10
                k-=1
        return curr

        
