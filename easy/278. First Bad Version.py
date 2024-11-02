# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s=0
        while s<=n:
            mid=(s+n)//2
            cur=isBadVersion(mid)
            prev=isBadVersion(mid-1)
            if cur and not prev:   return mid
            if prev:    return self.firstBadVersion(mid-1)
            s=mid+1
