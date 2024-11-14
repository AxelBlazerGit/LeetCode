class Solution:
    def viable(self,arr,q,n):
        stores=0
        for ele in arr:
            stores+=math.ceil(ele/q)
        return stores<=n
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        s=1
        e=max(quantities)
        minn=0
        while s<=e:
            mid=(s+e)//2
            if self.viable(quantities,mid,n):
                minn=mid
                e=mid-1
            else:
                s=mid+1
        return minn
