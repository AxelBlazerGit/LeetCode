class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        hash=defaultdict(int)
        champ=set()
        for src,dest in edges:
            hash[dest]+=1
        for i in range(n):
            if not hash[i]:
                champ.add(i)
        if len(champ)>1:
            return -1
        return champ.pop()
