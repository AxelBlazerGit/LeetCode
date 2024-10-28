class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev=0
        i=0
        while i<len(s):
            cur=0
            if s[i].isdigit():
                cur=int(s[i])
                i+=1
                while i<len(s) and s[i].isdigit():
                    cur*=10
                    cur+=int(s[i])
                    i+=1
                if cur <= prev:
                    return False
                prev=cur
            else:
                i+=1
        return True
