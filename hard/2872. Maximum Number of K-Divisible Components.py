class Solution:
    def dfs(self, node, k, incidence, values, hash):
        total = values[node]
        components = 0
        for node in incidence[node]:
            if node not in hash:
                hash.add(node)
                nextSum, nextComponent = self.dfs(node, k, incidence, values, hash)
                total += nextSum
                components += nextComponent
        if not total % k:
            components += 1
            total = 0
        return total, components

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if not edges:
            return 1
        incidence={}
        for v1,v2 in edges:
            if v1 not in incidence:
                incidence[v1] = []
            if v2 not in incidence:
                incidence[v2] = []
            incidence[v1].append(v2)
            incidence[v2].append(v1)
        visited=set([0])
        temp, components = self.dfs(0, k, incidence, values, visited)
        return components
