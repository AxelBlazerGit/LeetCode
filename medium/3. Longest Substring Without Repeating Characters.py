class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return len(s)
        hash=defaultdict(int)
        hash[s[0]]+=1
        subs=1
        l=0
        for r in range(1,len(s)):
            hash[s[r]]+=1
            while 2 in hash.values():
                hash[s[l]]-=1
                l+=1
            subs=max(subs,r-l+1)
            # if subs==26:
                # return subs
        return subs
