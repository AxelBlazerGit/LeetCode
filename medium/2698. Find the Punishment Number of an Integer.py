class Solution:
    def partition(self, s, x, idx = 0, cur = 0):
        if idx == len(s):
            return cur == x
        
        n = 0
        for i in range(idx, len(s)):
            n = n * 10 + int(s[i])
            if cur + n <= x:
                if self.partition(s, x, i + 1, cur + n):
                    return True
        
        return False

    def punishmentNumber(self, n: int) -> int:
        punishment = 0
        for i in range(1, n + 1):
            sq = str(i * i)
            if i%9 in {0,1} and self.partition(sq, i):
                punishment += i * i
        
        return punishment
