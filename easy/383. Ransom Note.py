class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash=defaultdict(int)
        for i in magazine:
            hash[i]+=1
        for i in ransomNote:
            hash[i]-=1
        return True if all(x>=0 for x in hash.values()) else False
