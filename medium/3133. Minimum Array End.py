class Solution:
    def minEnd(self, n: int, x: int) -> int:
        x = deque(bin(x)[2:])
        n_bin = bin(n - 1)[2:]
        n_len = len(n_bin)
        
        # Embed n-1 into the 0's of x
        j = n_len - 1 
        for i in range(len(x) - 1, -1, -1):
            if j < 0:
                break
            if x[i] == '0':
                x[i] = n_bin[j]
                j -= 1
        
        # prepend remaining bits
        while j >= 0:
            x.appendleft(n_bin[j])
            j -= 1

        return int("".join(x), 2)
# 4 100
# 5 101
# 6 110     
