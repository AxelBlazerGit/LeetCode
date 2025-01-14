class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hash=defaultdict(int)
        pca=[]
        for i in range(len(A)):
            hash[A[i]]+=1
            hash[B[i]]+=1
            pca.append(sum(1 for k in hash if hash[k]==2))
        return pca
