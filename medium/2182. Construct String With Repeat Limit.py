from heapq import heapify,heappush as push,heappop as ppop
class Solution:
    def ascii(self,x):
        return ord(x)-97
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        map=[[-self.ascii(x),y] for x,y in Counter(s).items()]
        heapify(map)
        repeat=list()
        while map:
            ch,f=ppop(map)
            ch=chr(97-ch)
            check=min(repeatLimit,f)
            repeat.append(ch*check)
            if f-check>0 and map:
                ch2,f2=ppop(map)
                ch2=chr(97-ch2)
                repeat.append(ch2)
                if f2-1:
                    push(map,[-self.ascii(ch2),f2-1])
                push(map,[-self.ascii(ch),f-check])
        return "".join(repeat)
