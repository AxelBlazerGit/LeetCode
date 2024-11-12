class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hash=[[0 for _ in range(len(text2)+1)] for __ in range(len(text1)+1)]
        for c1 in range(len(text1)-1,-1,-1):
            for c2 in range(len(text2)-1,-1,-1):
                if text1[c1]==text2[c2]:
                    hash[c1][c2]=hash[c1+1][c2+1]+1
                else:
                    hash[c1][c2]=max(hash[c1][c2+1],hash[c1+1][c2])
        return hash[0][0]
