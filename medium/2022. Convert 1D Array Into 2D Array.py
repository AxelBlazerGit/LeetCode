class Solution:
    def construct2DArray(self, original: List[int], rows: int, cols: int) -> List[List[int]]:
        if len(original)!=rows*cols:
            return []
        ans=[]
        curr=0
        for i in range(rows):
            ans.append([x for x in original[curr:curr+cols]])
            curr+=cols
        return ans
