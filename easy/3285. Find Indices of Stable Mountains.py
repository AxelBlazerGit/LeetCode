class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stables=[]
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                stables.append(i)
        return stables
