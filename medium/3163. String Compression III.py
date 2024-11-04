class Solution:
    def compressedString(self, word: str) -> str:
        streak=0
        cur=word[0]
        s=[]
        for i in range(len(word)):
            if word[i]==cur:
                if streak<9:    streak+=1
                else:
                    streak=1
                    s.append('9')
                    s.append(cur)
            else:
                s.append(str(streak))
                s.append(word[i-1])
                streak=1
                cur=word[i]
        s.append(str(streak))
        s.append(word[-1])
        return "".join(s)
