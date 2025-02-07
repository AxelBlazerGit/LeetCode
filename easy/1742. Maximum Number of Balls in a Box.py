class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def num(i):
            s=0
            while i:
                s+=i%10
                i//=10
            return s

        maxballs=1
        hash=defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            temp=num(i)
            hash[temp]+=1
            maxballs=max(maxballs,hash[temp])
        return maxballs
