class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[] # index mono stk
        wait=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            if stk:
                while stk and temperatures[stk[-1]]<t:
                    # print(stk)
                    wait[stk[-1]]=i-stk[-1]
                    stk.pop()
            stk.append(i)
        return wait
