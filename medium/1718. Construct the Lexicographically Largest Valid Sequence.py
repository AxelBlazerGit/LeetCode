class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ds=[0]*(2*n-1)
        hash=set()
        def bt(idx):
            if idx==len(ds):
                return True
            for x in range(n,0,-1):
                if (x in hash) or (x > 1 and ((idx + x) >= len(ds) or ds[idx + x])):
                    continue
                hash.add(x)
                ds[idx]=x
                if x>1:
                    ds[idx+x]=x
                temp=idx+1
                while temp<len(ds) and ds[temp]:
                    temp+=1

                if bt(temp):
                    return True
                
                hash.remove(x)
                ds[idx]=0
                if x>1:
                    ds[idx+x]=0
            return False
        bt(0)
        return ds
