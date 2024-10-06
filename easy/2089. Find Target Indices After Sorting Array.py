class Solution:
    def partition(self, arr, l, h):
        pivot = arr[l]
        L = l + 1
        R = h
        while L <= R:
            while L <= h and arr[L] <= pivot:
                L += 1
            while R >= l and arr[R] > pivot:
                R -= 1
            if L < R:
                arr[L], arr[R] = arr[R], arr[L]
                L += 1
                R -= 1
        arr[l], arr[R] = arr[R], arr[l]
        return R

    def quickS(self, arr, l, h):
        if l < h:
            pivot = self.partition(arr, l, h)
            self.quickS(arr, l, pivot - 1)
            self.quickS(arr, pivot + 1, h)

    def binSf(self, arr, x):
        s = 0
        e = len(arr) - 1
        idx = -1
        while s <= e:
            m = (s + e) // 2
            if arr[m] == x:
                idx = m
                e = m - 1
            elif arr[m] > x:
                e = m - 1
            else:
                s = m + 1
        return idx

    def binSl(self, arr, x):
        s = 0
        e = len(arr) - 1
        idx = -1
        while s <= e:
            m = (s + e) // 2
            if arr[m] == x:
                idx = m
                s = m + 1
            elif arr[m] > x:
                e = m - 1
            else:
                s = m + 1
        return idx

    def targetIndices(self, nums, target):
        self.quickS(nums, 0, len(nums) - 1)
        first_index = self.binSf(nums, target)
        last_index = self.binSl(nums, target)
        return [i for i in range(first_index, last_index + 1)] if first_index != -1 else []
