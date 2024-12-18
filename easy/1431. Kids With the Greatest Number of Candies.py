class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        celeb=max(candies)
        res=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=celeb:
                res.append(True)
            else:
                res.append(False)
        return res
