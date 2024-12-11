class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        freq = [[0] * (n + 1) for _ in range(26)]
        k = -1

        streak = 1
        for i in range(n):
            ascii = ord(s[i]) - ord('a')
            if i > 0 and s[i] == s[i - 1]:
                streak += 1
            else:
                streak = 1
            freq[ascii][streak] += 1

        for ch in range(26):
            for length in range(n, 0, -1):
                if length < n:
                    freq[ch][length] += freq[ch][length + 1]
                if freq[ch][length] >= 3:
                    k = max(k, length)
                    break

        return k
