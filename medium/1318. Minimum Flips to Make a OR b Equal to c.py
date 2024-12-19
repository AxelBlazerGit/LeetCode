class Solution:
    def makeItEqual(self, a: int, b: int, c: int)-> int:
        c=bin(c)[2:]
        a=bin(a)[2:]
        b=bin(b)[2:]
        l=max(len(a),len(b),len(c))
        a=a.zfill(l)[::-1]
        b=b.zfill(l)[::-1]
        c=c.zfill(l)[::-1]
        moves=0
        for x in range(len(c)):
            if c[x]=='1':
                if a[x]=='0' and b[x]=='0':
                    moves+=1
            else:
                if a[x]=='1':
                    moves+=1
                if b[x]=='1':
                    moves+=1
        return moves

    def minFlips(self, a: int, b: int, c: int) -> int:
        return self.makeItEqual(a,b,c)        
