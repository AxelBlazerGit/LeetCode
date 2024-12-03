class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces=set(spaces)
        new=list()
        for i in range(len(s)):
            if i not in spaces:
                new.append(s[i])
            else:
                new.append(" ")
                new.append(s[i])
        return "".join(new)
