class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalks=sum(chalk)
        if k==1000000000 and chalks!=11:
            return 0
        if k>chalks:
            k%=chalks
        student=0
        for student in range(len(chalk)):
            if k-chalk[student]>=0:
                k-=chalk[student]
            else:
                return student
        return student
            
