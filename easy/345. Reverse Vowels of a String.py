class Solution:
    def reverseVowels(self, s: str) -> str:
        hash=list()
        s=list(s)
        for i,c in enumerate(s):
            if c in "aeiouAEIOU":
                hash.append(c)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i]=hash.pop()
        return "".join(s)
