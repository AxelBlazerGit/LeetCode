class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        maxVal = float('-inf')  # Max value of current window
        minheap = list()  # Minheap with tuples (val, row, col)
        k = len(nums)
        
        # Push the first values of each list into the heap
        for i in range(k):
            maxVal = max(maxVal, nums[i][0])
            heapq.heappush(minheap, (nums[i][0], i, 0))
        
        min_L = 0  # Start of our range
        max_R = float('inf')  # End of range
        
        while True:
            currVal, r, c = heapq.heappop(minheap)
            
            # Update the range if smaller
            if max_R - min_L > maxVal - currVal:
                min_L = currVal
                max_R = maxVal
            
            # If possible, push next item of the list
            if c < len(nums[r]) - 1:
                heapq.heappush(minheap, (nums[r][c + 1], r, c + 1))
                maxVal = max(maxVal, nums[r][c + 1])
            else:
                break
        
        return list([min_L, max_R])
