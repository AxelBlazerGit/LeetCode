class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        n=min(len(word1),len(word2))
        merge=list()
        while i<n:
            merge.append(word1[i])
            merge.append(word2[i])
            i+=1
        while i<len(word1):
            merge.append(word1[i])
            i+=1
        while i<len(word2):
            merge.append(word2[i])
            i+=1
        return "".join(merge)
