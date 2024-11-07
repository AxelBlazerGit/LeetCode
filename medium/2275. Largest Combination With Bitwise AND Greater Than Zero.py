class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxbit=0
        for exp in range(32):
            bit=0
            for x in candidates:
                bit+=1 if (1<<exp)&x else 0
            maxbit=max(maxbit,bit)
        return maxbit
