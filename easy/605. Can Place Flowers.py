class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        for i in range(len(flowerbed)):
            if not flowerbed[i]:
                l=(not i) or (not flowerbed[i-1])
                r= (i==len(flowerbed)-1) or (not flowerbed[i+1])
                if l+r==2:
                    flowerbed[i]=1
                    n-=1
                    if not n:
                        return True
        return False
