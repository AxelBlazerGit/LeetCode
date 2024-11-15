class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # find the longest increasing sequence (lis) from the start of the array
        # find the longest decreasing sequence (lds) from the end of the array
        # if lis and lds overlap or touch, the array is already sorted, so return 0
        # initialize the answer as the length of the lds since removing it ensures a sorted array
        # iterate through the lis and try to merge it with the lds by finding the farthest valid point in lds
        # shrink the answer whenever merging is possible
        n = len(arr)
        l, r = 0, n - 1
        while l + 1 < n and arr[l + 1] >= arr[l]:
            l += 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        if l >= r:
            return 0
        i = 0
        ans = r
        while i <= l:
            while r < n and arr[r] < arr[i]:
                r += 1
            ans = min(ans, r - i - 1)
            i += 1
        return ans
