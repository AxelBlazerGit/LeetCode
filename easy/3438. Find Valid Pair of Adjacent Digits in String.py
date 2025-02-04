class Solution:
    def findValidPair(self, s: str) -> str:
        def num(x):
            return int(x)==freq[x]
        freq=Counter(s)
        for i in range(len(s)-1):
                if s[i]!=s[i+1] and num(s[i]) and num(s[i+1]):
                    return s[i]+s[i+1]
        return ""
