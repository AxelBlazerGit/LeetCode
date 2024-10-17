class Solution:
    def maximumSwap(self, num: int) -> int:
        # Find rightmost maximum digit to swap with current
        # Perform a swap if beneficial
        num = list(str(num))
        for i in range(len(num)):
            max_idx = i
            for j in range(i + 1, len(num)):
                if num[j] >= num[max_idx]:
                    max_idx = j
            if max_idx != i and num[i] != num[max_idx]:
                num[i], num[max_idx] = num[max_idx], num[i]
                break
        return int(''.join(num))
