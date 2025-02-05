class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,-1
        n=len(numbers)
        while l<n+r:
            temp=numbers[l]+numbers[r]
            if temp==target:
                return [l+1,n+r+1]
            elif temp>target:
                r-=1
            else:
                l+=1
