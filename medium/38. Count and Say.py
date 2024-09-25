class Solution:
    def countAndSay(self, n: int) -> str:
        hash={}
        hash[1]="1"
        hash[2]="11"
        hash[3]="21"
        if n in hash:
            return hash[n]
        for i in range(3,n+1):
            temp=str(hash[i-1])
            hashTemp=""
            currStreak=1
            for j in range(1,len(temp)):
                if temp[j]!=temp[j-1]:
                    hashTemp+=f"{currStreak}{temp[j-1]}"
                    currStreak=1
                else:
                    currStreak+=1
                hash[i]=hashTemp+f"{currStreak}{temp[-1]}"
        return hash[n]
