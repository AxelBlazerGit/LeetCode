class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hash={}
        temp=sorted(set(arr))
        cur=1
        for i in temp:
            hash[i]=cur
            cur+=1
        for i in range(len(arr)):
            arr[i]=hash[arr[i]]
        return arr
