class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash=[0]*26
        for i in s:
            hash[ord(i)-97]+=1
        for i in range(len(s)):
            if hash[ord(s[i])-97]==1:
                return i
        return -1
