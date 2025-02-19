class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        l,r=1,3*(2**(n-1))
        choose=['a','b','c']
        happy=[]
        for i in range(n):
            cur=l
            size=(r-l+1)//len(choose)
            for ch in choose:
                if k in range(cur,cur+size):
                    happy.append(ch)
                    l,r=cur,cur+size-1
                    choose=[ch for ch in ['a','b','c'] if ch!=happy[-1]]
                    break
                cur+=size
        return "".join(happy)
