class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = [0]
        hash = set()
        def bt(idx):
            if idx == len(s):
                res[0] = max(res[0], len(hash))
                return
            for i in range(idx, len(s)):
                temp = s[idx:i+1]
                # unique
                if temp not in hash:
                    hash.add(temp)
                    # backtrack
                    bt(i + 1)
                    # more possible substrings
                    hash.remove(temp)
        bt(0)
        return res[0]
