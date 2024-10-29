class Solution:
    def climbStairs(self, n: int) -> int:
        prev=1
        cur=1
        if n==cur:  return n
        for i in range(n-1):
            prev,cur=cur,prev+cur
        return cur
