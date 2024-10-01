class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hash = {}
        for i in arr:
            remainder = i % k
            if remainder < 0:
                remainder += k
            if remainder in hash:
                hash[remainder] += 1
            else:
                hash[remainder] = 1
        for r in hash:
            if r == 0:
                if hash[r] % 2 != 0:
                    return False
            elif 2 * r == k:
                if hash[r] % 2 != 0:
                    return False
            else:
                if k - r not in hash or hash[r] != hash[k - r]:
                    return False
        return True
