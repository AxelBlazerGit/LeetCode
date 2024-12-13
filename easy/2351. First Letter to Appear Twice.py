class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash=[0]*26
        for i in s:
            hash[ord(i)-97]+=1
            if hash[ord(i)-97]==2:
                return i
