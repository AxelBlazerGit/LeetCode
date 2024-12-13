class Solution:
    def frequencySort(self, s: str) -> str:
        hash=Counter(s)
        hash=sorted(hash.items(), key=lambda x: -x[1])
        # heapq.heapify()
        new=[]
        for ch,f in hash:
            if f:
                new.extend([ch]*f)
        return "".join(new)
