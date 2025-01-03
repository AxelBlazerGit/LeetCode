class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur=mx=0
        vowels=set("aeiou")
        for i in range(k):
            if s[i] in vowels:
                cur+=1
        mx=cur
        if mx==k:
            return k
        for i in range(k,len(s)):
            if s[i] in vowels:
                cur+=1
            if s[i-k] in vowels:
                cur-=1
            mx=max(mx,cur)
            if mx==k:
                return k
        return mx
