class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        def cost():
            delta=0
            for i in range(len(arr)):
                delta+=abs(arr[i]-brr[i])
            return delta
        initial=cost()
        arr.sort()
        brr.sort()
        return min(cost()+k,initial)
        # return min(cost(),k+cost())
