class Solution:
    def check(self,s,goal,idx):
        if idx==len(s): return False
        s=s[1:]+s[0]
        if s==goal: return True
        return self.check(s,goal,idx+1)
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):   return False
        # return self.check(s,goal,0)
        return goal in s+s
