class Solution:
    def binSf(self,nums,x):
        ans,s,e=-1,0,len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==x:
                ans=mid
                e=mid-1
            elif nums[mid]>x:
                e=mid-1
            else:
                s=mid+1
        return ans
    def binSl(self,nums,x):
        ans,s,e=-1,0,len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==x:
                ans=mid
                s=mid+1
            elif nums[mid]>x:
                e=mid-1
            else:
                s=mid+1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binSf(nums,target),self.binSl(nums,target)]
