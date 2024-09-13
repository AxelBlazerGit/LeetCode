class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
    # Find the {1stDIP} i.e. the first number that is smaller than the number to its ajdacent right.
    # noDIP=>return reversed arr
    # else: swap position idx and rightmost {i} that obeys arr[i]>arr[idx]
    # reverse arr from idx+1:end and return 

        idx=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
        if idx==-1:
            nums=nums.reverse()
            return
        for i in range(n-1,idx,-1):
            if nums[i]>nums[idx]:
                nums[i],nums[idx]=nums[idx],nums[i]
                break
        nums[idx+1:] = reversed(nums[idx+1:])
        return
