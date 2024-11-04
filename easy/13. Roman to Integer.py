class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        val=0
        i=0
        while i<len(s):
            if i==len(s)-1:
                val+=hash[s[i]]
                break
            if hash[s[i]]>=hash[s[i+1]]:
                val+=hash[s[i]]
                i+=1
            else:
                val+=hash[s[i+1]]-hash[s[i]]
                i+=2
        return val
