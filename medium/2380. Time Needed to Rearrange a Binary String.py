class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        n = len(s)
        seconds = 0
        
        while True:
            flag = False
            i = 0
            while i < n - 1:
                if s[i] == '0' and s[i + 1] == '1':
                    s[i], s[i + 1] = s[i + 1], s[i]
                    flag = True
                    i += 1
                i += 1
            if not flag:
                return seconds
            seconds += 1
