class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash={}
        for i in range(len(s)):
            if s[i] in hash:
                hash[s[i]]+=1
            else:
                hash[s[i]]=1
            if t[i] in hash:
                hash[t[i]]-=1
            else:
                hash[t[i]]=-1
        return False if set(hash.values())!=set([0]) else True
