class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        val=0
        for w in strs:
            if any(ord(x) in range(97,122+1) for x in w):
                val=max(val,len(w))
            else:
                val=max(val,int(w))
        return val
