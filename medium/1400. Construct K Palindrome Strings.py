class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        return sum(i%2 for i in Counter(s).values())<=k
