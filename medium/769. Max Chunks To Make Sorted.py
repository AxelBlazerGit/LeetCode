class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        splits=sum=0
        for idx,ele in enumerate(arr):
            sum+=ele
            if sum==idx*(idx+1)//2:
                splits+=1
        return splits
