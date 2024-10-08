class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        pre=post=0
        for ch in s:
            pre += 1 if ch == '(' else -1
            if pre < 0:
                post+=1
                pre = 0
        return pre + post
