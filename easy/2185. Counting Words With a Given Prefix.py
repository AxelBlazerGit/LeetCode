class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        k=len(pref)
        prefix=0
        for w in words:
            if len(w)>=k:
                if w[:k]==pref:
                    prefix+=1
        return prefix
