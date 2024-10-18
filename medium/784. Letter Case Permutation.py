class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        lcp=[]
        temp=""
        def bt(temp,idx):
            if idx==len(s):
                lcp.append(temp)
                return
            if s[idx].isalpha():
                bt(temp+s[idx].lower(),idx+1)
                bt(temp+s[idx].upper(),idx+1)
            else:
                bt(temp+s[idx],idx+1)
        bt(temp,0)
        return lcp 
