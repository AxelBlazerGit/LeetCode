class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[1]*n
        lds=lis[:]
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i]=max(lis[i],lis[j]+1)
        for i in range(n-1,-1,-1):
            for j in range(n-1,i-1,-1):
                if nums[i]>nums[j]:
                    lds[i]=max(lds[i],lds[j]+1)
        remove=0
        for i in range(1,n-1):
            if lis[i]>1 and lds[i]>1:
                remove=max(remove,lis[i]+lds[i])
        return n-remove+1
