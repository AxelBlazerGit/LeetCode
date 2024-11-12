class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        st=e=0
        size=1
        for i in range(len(s)):
            odd=check(i,i)
            if odd>size:
                st=i-odd//2
                e=i+odd//2
                size=odd
            even=check(i,i+1)
            if even>size:
                st=i-even//2+1
                e=i+even//2
                size=even
        return s[st:e+1]
