class Solution:
    def removeStars(self, s: str) -> str:
        nostar=list()
        for i in s:
            if i!='*':
                nostar.append(i)
            elif nostar:
                nostar.pop()
        return "".join(nostar)
