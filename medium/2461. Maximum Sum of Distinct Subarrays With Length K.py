class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        hash={}
        cur=subsum=start=0
        for i in range(n):
            if nums[i] in hash and hash[nums[i]]>=start:
                dupe=hash[nums[i]]
                while start<=dupe:
                    cur-=nums[start]
                    start+=1
            hash[nums[i]]=i
            cur+=nums[i]
            if i-start+1==k:
                subsum=max(subsum,cur)
                cur-=nums[start]
                start+=1
        return subsum if subsum else 0
