class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans=0
        for i in range(int(total/cost1)+1):
            ans+=(total-cost1*i)//cost2+1
        return ans
