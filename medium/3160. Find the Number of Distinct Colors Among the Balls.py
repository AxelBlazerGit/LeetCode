class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hash=defaultdict(set)
        seen={} #ball,col
        colors=[0]*len(queries)
        for i,(ball,col) in enumerate(queries):
            if ball in seen:
                hash[seen[ball]].remove(ball)
                if not hash[seen[ball]]:
                    del hash[seen[ball]]
            hash[col].add(ball)
            seen[ball]=col
            colors[i]=len(hash)
        return colors
# 0 0 0 0 0 = 0
# 0 4 0 0 0 = 1
# 0 4 5 0 0 = 2
# 0 3 5 0 0 = 2
# 0 3 5 4 0 = 3


# 0 0 0 0 0
# 1 0 0 0 0 = 1
# 1 2 0 0 0 = 2
# 1 2 2 0 0 = 2
# 1 2 2 4 0 = 3
# 1 2 2 4 5 = 4
