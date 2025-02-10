class Solution:
    def clearDigits(self, s: str) -> str:
        stk=[]
        for c in s:
            if c not in "1234567890":
                stk.append(c)
            else:
                if stk:
                    stk.pop()
        return "".join(stk)
