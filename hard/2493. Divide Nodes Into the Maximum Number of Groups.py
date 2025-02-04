class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        def dist(st):
            dist = {st: 1}
            dq = deque([st])
            maxDist = 1

            while dq:
                node = dq.popleft()
                for v in graph[node]:
                    if v not in dist:
                        dist[v] = dist[node] + 1
                        maxDist = max(maxDist, dist[v])
                        dq.append(v)

            return maxDist

        def dfs(node, code):
            stk = [(node, code)]
            component = []
            bipart = True

            while stk:
                cur, col = stk.pop()
                if cur in color:
                    if color[cur] != col:
                        return [], False
                    continue

                color[cur] = col
                component.append(cur)

                for v in graph[cur]:
                    stk.append((v, 3 - col))

            return component, bipart

        color = {}
        groups = 0

        for node in range(1, n + 1):
            if node not in color:
                component, bipart = dfs(node, 1)
                if not bipart:
                    return -1
                groups += max(dist(v) for v in component)

        return groups
