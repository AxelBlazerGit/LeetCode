class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumReq = ((len(rolls) + n) * mean) - sum(rolls)
        # print(f"Initial sum required: {sumReq}")
        
        if sumReq == 0 or sumReq / n > 6 or sumReq < 0 or n > sumReq:
            # print(f"Returning empty list due to invalid conditions.")
            return []
        
        ans = []
        for i in range(n):
            rollsRemaining = n - i
            for j in range(6, 0, -1):
                if (sumReq - j) >= rollsRemaining - 1:
                    ans.append(j)
                    sumReq -= j
                    # print(f"Added {j} to ans. Remaining sum: {sumReq}, Places to fill more: {rollsRemaining - 1}")
                    break
        
        # print(f"Final answer list: {ans}")
        return ans




# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         sumReq=((len(rolls)+n)*mean)-sum(rolls)
#         if sumReq==0 or sumReq//n>6 or sumReq<0:
#             return []
#         ans=[]
#         for i in range(n):
#             rollsRemaining=n-i+1
#             for j in range(6,-1,-1):
#                 if (sumReq-j)>=rollsRemaining:
#                     ans.append(j)
#                     sumReq-=j
#                     break

#         return ans
