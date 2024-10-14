class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        swm = []
        queue = collections.deque()  # storing indices
        for i in range(len(nums)):
            # shrink window
            if queue and queue[0] == i - k:
                queue.popleft()
            # if queue has form [x, x+r] => smaller ele , larger ele: then pop
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            # push from temp heap
            if i >= k - 1:
                swm.append(nums[queue[0]])
        return swm
