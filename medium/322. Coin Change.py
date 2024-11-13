class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hash=[10**9]*(amount+1)
        coins.sort()
        hash[0]=0
        for i in range(1,amount+1):
            for c in coins:
                delta=i-c
                if delta<0:
                    break
                hash[i]=min(hash[i],1+hash[delta])
        return hash[-1] if hash[-1]!=10**9 else -1
