class Solution:
    # leetcode 2337
    def canChange(self, start: str, target: str) -> bool:
        start=[(i,idx) for idx,i in enumerate(start) if i in 'LR']
        target=[(i,idx) for idx,i in enumerate(target) if i in 'LR']
        if len(start)!=len(target):
            return False
        
        for i in range(len(start)):
            if start[i][0]!=target[i][0]:
                return False
            
            if start[i][0]=='L':
                if start[i][1]<target[i][1]:
                    return False
            if start[i][0]=='R':
                if start[i][1]>target[i][1]:
                    return False
            
        return True

    def canTransform(self, start: str, result: str) -> bool:
        return self.canChange(start,result)
