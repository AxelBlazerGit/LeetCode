class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        palins=set()
        l=set()
        r=Counter(s)
        for c in s:
            r[c]-=1
            for ch in l:
                if r[ch]:
                    palins.add((c,ch))
            l.add(c)
        return len(palins)
