class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0]!=str2[0] or set(str1)!=set(str2):
            return ""
        limit=min(len(str1),len(str2))
        cur=limit
        while cur-1:
            mul1,mul2=len(str1)//cur,len(str2)//cur
            if (str1[:cur])*mul1==str1 and (str2[:cur])*mul2==str2:
                return str1[:cur]
            cur-=1
        return str1[:cur] if (str1[:cur])*(len(str1)//cur)==str1 and (str2[:cur])*(len(str2)//cur)==str2 else ""
