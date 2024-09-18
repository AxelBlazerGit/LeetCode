class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for i in strs:
            temp="".join(sorted(i))
            if temp in hash:
                hash[temp].append(i)
            else:
                hash[temp]=[i]
        return list(hash.values())
