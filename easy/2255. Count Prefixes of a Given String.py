class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefixes=0
        for i in words:
            k=len(i)
            prefixes+=1 if s[:k]==i else 0
        return prefixes
