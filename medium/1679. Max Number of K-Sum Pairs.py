class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        arr=Counter(nums)
        ops=0
        for i in list(arr.keys()):
            j=k-i
            if j in arr:
                if i==j:
                    ops+=arr[i]//2
                else:
                    ops+=min(arr[i],arr[j])
                del arr[i]
                if j in arr:
                    del arr[j]
        return ops
