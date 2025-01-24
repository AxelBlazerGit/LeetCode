class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        states={}
        def safe(v):
            if v in states:
                return states[v]
            states[v]=False
            for e in graph[v]:
                if not safe(e):
                    return states[v]
            states[v]=True
            return states[v]
        nodes=[]
        for i in range(len(graph)):
            if safe(i):
                nodes.append(i)
        return nodes
