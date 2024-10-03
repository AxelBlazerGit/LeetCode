class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # hash to track prefix sums modulo p, initialize with 0=> -1.
        # iterate over the array, updating prefix sums and looking for subarrays where 
        # the difference between the current prefix and excess is in the hash map.

        sm = sum(nums)
        excess = sm % p
        if not excess:
            return 0
        
        hash = {0: -1}
        ans = len(nums)
        cur = 0
        
        for idx, ele in enumerate(nums):
            cur += ele
            cur %= p
            mod = (cur - excess + p) % p
            if mod in hash:
                ans = min(ans, idx - hash[mod])
            hash[cur] = idx
        
        return ans if ans != len(nums) else -1
