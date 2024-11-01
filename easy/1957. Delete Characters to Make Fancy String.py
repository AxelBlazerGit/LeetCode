class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:    return s
        fancy = [s[0], s[1]]
        for i in range(2,len(s)):
            fancy.append(s[i])
            if fancy[-1]==fancy[-2] and fancy[-2]==fancy[-3]:
                fancy.pop()
        return "".join(fancy)
