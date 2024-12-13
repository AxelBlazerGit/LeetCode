class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        hash={}
        def pow(x):
            if x in hash:
                return hash[x]
            if x==1:
                return 0
            if x&1:
                hash[x] = pow(3*x+1)+1
            else:
                hash[x] = pow(x//2)+1
            return hash[x]
        temp=[(ele,pow(ele)) for ele in range(lo,hi+1)]
        temp.sort(key= lambda x:x[1])
        return temp[k-1][0]
