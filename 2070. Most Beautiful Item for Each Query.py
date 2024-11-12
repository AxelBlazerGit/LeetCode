class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries=sorted([q,idx] for idx,q in enumerate(queries))
        beauty=0
        ans=[0]*len(queries)
        ptr=0
        for q,idx in queries:
            while ptr<len(items) and items[ptr][0]<=q:
                beauty=max(beauty,items[ptr][1])
                ptr+=1
            ans[idx]=beauty
        return ans
