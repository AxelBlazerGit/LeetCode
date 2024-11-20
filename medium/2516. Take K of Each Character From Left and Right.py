class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        hash = [0] * 3
        n = len(s)
        if not k:   return 0
        for i in s:
            hash[ord(i) - 97] += 1
        if any(count < k for count in hash):
            return -1
        temp = [0, 0, 0]
        l = size = 0
        for r in range(n):
            temp[ord(s[r]) - 97] += 1
            while l <= r and any(hash[i] - temp[i] < k for i in range(3)):
                temp[ord(s[l]) - 97] -= 1
                l += 1
            size = max(size, r - l + 1)
        return n - size
