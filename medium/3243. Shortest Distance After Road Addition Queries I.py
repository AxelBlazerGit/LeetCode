class Solution:
    def shortest(self,road,n):
        dq = deque([(0, 0)])  # (cur, shortest)
        hash = set([(0, 0)])
        while dq:
            cur,shortest=dq.popleft()
            if cur==n-1:
                return shortest
            for next in road[cur]:
                if next not in hash:
                    hash.add(next)
                    dq.append((next, shortest + 1))
                    
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        road=[[x+1] for x in range(n)]
        path=[]
        for city1,city2 in queries:
            road[city1].append(city2)
            path.append(self.shortest(road,n))
        return path
