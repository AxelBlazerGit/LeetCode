class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n<3: return False
        # if n!=len(set(arr)):    return False
        piv=0
        cur=arr[0]
        piv=0
        while piv+1<n and arr[piv+1]>arr[piv]:
            piv+=1
        if not piv or piv==n-1: return False
        while piv+1<n and arr[piv+1]<arr[piv]:
            piv+=1
        return piv==n-1
