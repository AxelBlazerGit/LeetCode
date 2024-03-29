class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s=0
        e=len(arr)-1
        if e==2:
            return e-1
        while(s<e):
            mid=int(s+(e-s)/2)
            if arr[mid]>arr[mid-1] and arr[mid+1]<arr[mid]:
                return mid
            if arr[mid]>arr[mid-1]:
                s=mid
            else:
                e=mid
        return s # just to adjust syntax
