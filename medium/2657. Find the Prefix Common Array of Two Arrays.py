class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hash=[0]*(len(A)+1)
        pca=[0]*len(A)
        cur=0
        for i in range(len(A)):
            hash[A[i]]+=1
            if hash[A[i]]==2:
                cur+=1
            hash[B[i]]+=1
            if hash[B[i]]==2:
                cur+=1
            pca[i]=cur
            
        return pca
# 1 3 2 4
# 3 1 2 4
# 0 1 0 1 0
# 0 2 0 2 0
# 0 2 2 2 0
# 0 

# class Solution:
#     def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
#         hash=defaultdict(int)
#         pca=[]
#         for i in range(len(A)):
#             hash[A[i]]+=1
#             hash[B[i]]+=1
#             pca.append(sum(1 for k in hash if hash[k]==2))
#         return pca
