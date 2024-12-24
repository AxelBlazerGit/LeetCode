class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        def diameterTree(adj, node, parent):
            dia = 0
            heap = [0,0]

            for neighbor in adj[node]:
                if neighbor != parent:
                    nDia, nPath = diameterTree(adj, neighbor, node)
                    dia = max(dia, nDia)
                    heappush(heap, nPath)
                    heappop(heap)

            dia = max(dia, sum(heap))

            return [dia, 1 + max(heap) if heap else 0]

        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        for node1, node2 in edges1:
            adj1[node1].append(node2)
            adj1[node2].append(node1)

        for node1, node2 in edges2:
            adj2[node1].append(node2)
            adj2[node2].append(node1)

        dia1, _ = diameterTree(adj1, 0, -1)
        dia2, _ = diameterTree(adj2, 0, -1)

        return max(dia1, dia2, ceil(dia1 / 2) + ceil(dia2 / 2) + 1)
