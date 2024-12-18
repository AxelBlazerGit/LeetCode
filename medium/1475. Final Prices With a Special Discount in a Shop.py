class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk=[]
        res=[]
        n=len(prices)
        for i in range(n):
            while stk and stk[-1]>prices[n-i-1]:
                stk.pop()
            if not stk:
                res.append(prices[n-i-1])
            else:
                res.append(prices[n-i-1]-stk[-1])
            stk.append(prices[n-i-1])
        return res[::-1]
