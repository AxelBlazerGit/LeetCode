class Solution:
    def binS(self, arr, skip, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val, mid_idx = arr[mid]
            if mid_val == target and mid_idx != skip:
                return 1
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return 0
    def checkIfExist(self, arr: List[int]) -> bool:
        arr=[(ele,idx) for idx,ele in enumerate(arr)]
        arr.sort()
        for ele,idx in arr:
            if self.binS(arr,idx,2*ele):
                return True
        return False
