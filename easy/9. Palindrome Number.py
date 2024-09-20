class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        bk=x
        while bk:
            rev=rev*10+bk%10
            bk//=10
        if rev==x:
            return True
        return False
