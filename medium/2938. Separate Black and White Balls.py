class Solution:
    def minimumSteps(self, s: str) -> int:
        z=0
        steps=0
        for idx,ele in enumerate(s):
            if ele=='0':
                steps+=idx-z
                z+=1
        return steps
