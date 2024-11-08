class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        #  To maximize the XOR with a value `k` less than `2^maximumBit`,
        #    use a "flipper" mask `flipper` set to `2^maximumBit - 1`, which has all bits set to 1 up to `maximumBit`.
        #  For each query, find `k` by XORing `xor` with `flipper`. This ensures that `k` has all bits set to 1
        #    wherever `xor` has 0, giving the maximum XOR result.
        #  Append `k` to the `query` list and remove the last element in `nums` from `xor` by XORing it out.
        #  Repeat for each query, progressively shrinking `nums` from the end and adjusting `xor`.
        
        xor = 0
        for i in nums: xor ^= i
        n = len(nums)
        flipper = (1 << maximumBit) - 1
        query = []
        for i in range(n):
            query.append(xor ^ flipper)
            xor ^= nums[n - 1 - i]
        return query
