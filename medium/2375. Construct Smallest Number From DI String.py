class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stk=[]
        num=1
        sn=['']*(len(pattern)+1)

        for idx,ch in enumerate(pattern):
            stk.append(idx)
            if ch=='I':
                while stk:
                    sn[stk.pop()]=str(num)
                    num+=1
        
        stk.append(len(pattern))
        while stk:
            sn[stk.pop()]=str(num)
            num+=1

        return "".join(sn)
