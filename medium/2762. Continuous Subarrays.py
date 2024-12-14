class Solution:
   # we through array with right pointer while keeping track of min and max values within current window
   # if at any point diff between curmax and curmin becomes greater than 2 we need to adjust left pointer to shrink window
   # we move left pointer one step to right and update curmin and curmax accordingly
   # after adjusting left pointer we calculate number of subarrays formed by window between left and right pointers
   def continuousSubarrays(self, nums: List[int]) -> int:
     curmin = float('inf')
     curmax = -curmin
     left = ans = 0
    
     for right in range(len(nums)):
       curmin = min(curmin, nums[right])
       curmax = max(curmax, nums[right])
      
       if curmax - curmin > 2:
       window = right - left
       ans += window * (window + 1)
      
       left = right
       curmin = curmax = nums[right]
       
       while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
       left -= 1
       curmin = min(curmin, nums[left])
       curmax = max(curmax, nums[left])
       
       if left < right:
       window = right - left
       ans -= window * (window + 1)
     window = len(nums) - left
     return (ans + window * (window + 1)) // 2
