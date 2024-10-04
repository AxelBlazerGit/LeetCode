class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s=sum(skill)
        n=len(skill)
        teams=n//2
        if s%teams:
            return -1
        chemistry=s//teams
        hash=Counter(skill)
        ans=0
        for p1,val in hash.items():
            p2=chemistry-p1
            if p2 not in hash or hash[p2]-val:
                return -1
            ans+=p1*p2*val
        return ans//2

                
