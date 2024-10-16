class Solution:
    def reorganizeString(self, s: str) -> str:
        # impossible: max freq character exceeds (n+1)//2 freq
        # pop two most frequent characters from hash
        # append to result and decrease frequency
        # push back to hash if remaining count>0
        # if one character is left in hash, append to result
        # return result string or "" as atq
        hash = [(-freq, ch) for ch, freq in Counter(s).items()]
        heapq.heapify(hash)
        if hash and -hash[0][0] > (len(s) + 1) // 2:
            return ""
        result = []
        while len(hash)>1:
            freq1, char1 = heapq.heappop(hash)
            freq2, char2 = heapq.heappop(hash)

            result.append(char1)
            result.append(char2)

            if freq1 + 1 < 0:
                heapq.heappush(hash, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(hash, (freq2 + 1, char2))

        if hash:
            result.append(heapq.heappop(hash)[1])

        return ''.join(result)
