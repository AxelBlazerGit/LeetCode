class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start,goal=bin(start)[2:][::-1],bin(goal)[2:][::-1]
        flips=0
        mn,mx=(start,goal) if len(start)<=len(goal) else (goal,start)
        for i in range(len(mn)):
            if mn[i]!=mx[i]:
                flips+=1
        for i in range(len(mn),len(mx)):
            if mx[i]=='1':
                flips+=1
        return flips
