class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # - initialize a deque to maintain a sliding window of prefix sums and indices, and track the shortest subarray length.
        # - use a prefix sum `cur` to calculate the cumulative sum as we iterate through the array.
        # - if `cur >= k`, update the shortest subarray length since the subarray from index 0 to the current index satisfies the condition.
        # - use the deque to manage valid windows:
        #   - while the difference between the current prefix sum and the smallest prefix sum in the deque is >= k,
        #     remove the smallest prefix sum from the deque and update the shortest subarray length.
        #   - maintain a monotonic increasing order in the deque by removing elements from the back that are >= the current prefix sum.
        #     this ensures the deque always stores potential starting points for valid subarrays.
        # - append the current prefix sum and index to the deque.
        # - after processing, return the shortest subarray length if it was updated; otherwise, return -1 if no valid subarray exists.

        ans=10**5+1
        cur=0
        dq=deque() # prefixSum,Endidx
        for i in range(len(nums)):
            cur+=nums[i]
            if cur>=k:
                ans=min(ans,i+1)

            while dq and cur-dq[0][0]>=k:
                temp,idx=dq.popleft()
                ans=min(ans,i-idx)
            
            while dq and dq[-1][0]>=cur:
                dq.pop()
            
            dq.append((cur,i))
        return ans if ans!=10**5+1 else -1
