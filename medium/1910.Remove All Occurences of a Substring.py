# stack
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk=[]
        n=len(part)
        part=list(part)
        for c in s:
            stk.append(c)
            if len(stk)>=n and stk[-n:]==part:
                stk[-n:]=[]
        return "".join(stk)


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            idx = s.find(part)
            if idx != -1:
                s = s[:idx] + s[idx+len(part):]
        return s
