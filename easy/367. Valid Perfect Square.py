class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        s=1
        e=num
        while s<=e:
            mid=s+e
            mid//=2
            temp=mid*mid
            if temp==num:
                return True
            elif temp>num:
                e=mid-1
            else:
                s=mid+1
        return False
