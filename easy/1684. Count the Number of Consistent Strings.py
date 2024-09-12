class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        consistent=0
        for i in words:
            if set(i)==allowed or set(i).issubset(allowed):
                consistent+=1
        return consistent
