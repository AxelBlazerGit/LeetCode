class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1,hash2=[0]*26,[0]*26
        n1=len(s1)
        for i in s1:
            hash1[ord(i)-97]+=1
        for i in range(len(s2)):
            hash2[ord(s2[i])-97]+=1
            if i>=n1:
                hash2[ord(s2[i-n1])-97]-=1
            if hash1==hash2:
                return True
        return False
