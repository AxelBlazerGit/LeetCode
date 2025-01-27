class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        G=defaultdict(list)
        for pre,c in prerequisites:
            G[c].append(pre)

        hash=defaultdict(set)
        def isPre(c):
            if c not in hash:
                for pre in G[c]:
                    hash[c]|=isPre(pre)
            hash[c].add(c)
            return hash[c]
        
        for c in range(numCourses):
            isPre(c)

        pre=[False]*len(queries)

        for i, (sub, main) in enumerate(queries):
            if sub in hash[main]:
                pre[i] = True

        return pre
