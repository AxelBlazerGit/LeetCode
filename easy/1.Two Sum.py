class Solution:
    # def partition(self, arr, low, high):
    #     pivot = arr[low]
    #     i = low
    #     j = high

    #     while i < j:
    #         while arr[i] <= pivot and i <= high - 1:
    #             i += 1

    #         while arr[j] > pivot and j >= low + 1:
    #             j -= 1

    #         if i < j:
    #             arr[i], arr[j] = arr[j], arr[i]

    #     arr[low], arr[j] = arr[j], arr[low]
    #     return j

    # def qs(self, arr, low, high):
    #     if low < high:
    #         p_index = self.partition(arr, low, high)
    #         self.qs(arr, low, p_index - 1)
    #         self.qs(arr, p_index + 1, high)
    #     return arr

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # hash_map = {}
        # for i in range(len(nums)):
        #     hash_map[i] = nums[i]

        # nums = self.qs(nums, 0, len(nums) - 1)

        # i = 0
        # j = len(nums) - 1

        # while i < j:
        #     if nums[i] + nums[j] > target:
        #         j -= 1
        #     elif nums[i] + nums[j] < target:
        #         i += 1
        #     else:
        #         first_index = next(key for key, value in hash_map.items() if value == nums[i])
        #         second_index = next(key for key, value in hash_map.items() if value == nums[j] and key != first_index)
        #         return [first_index, second_index]

        # return None
        # #############################
        hash={}
        count=0
        for i in nums:
            if target-i in hash:
                return [hash[target-i],count]
            hash[i]=count
            count+=1
