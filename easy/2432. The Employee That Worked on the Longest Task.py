class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        id,cur=logs[0][0],logs[0][1]
        for i in range(1,len(logs)):
            if logs[i][1]-logs[i-1][1]>cur:
                cur= logs[i][1]-logs[i-1][1]
                id=logs[i][0]
            elif logs[i][1]-logs[i-1][1]==cur:
                cur= logs[i][1]-logs[i-1][1]
                id=min(id,logs[i][0])
        return id
