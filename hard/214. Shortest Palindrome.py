class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        rev=s[::-1]
        n=len(s)
        for i in range(n):
            if s[:n-i] == rev[i:]:
                return rev[:i] + s
        # if s==s[::-1]:
        #     return s
        # hash = defaultdict(int)
        # for ch in s:
        #     hash[ch] += 1
        # def palindrome(counts):
        #     odd_count = sum(1 for val in counts.values() if val % 2 == 1)
        #     return odd_count <= 1
        # for i in range(len(s) - 1, -1, -1):
        #     hash[s[i]] -= 1
        #     if palindrome(hash):
        #         return s[i:] + s
        # return s[1:][::-1] + s
# i=0
# return s[i:]+s

# Pracecar
# racecarPracecar
