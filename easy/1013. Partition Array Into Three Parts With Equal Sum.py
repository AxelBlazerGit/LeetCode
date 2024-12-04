class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3:
            return False
        cur, split = 0, 0
        for i in arr:
            cur += i
            if cur == s // 3:
                cur = 0
                split += 1
                if split == 3:
                    return True
        return False
