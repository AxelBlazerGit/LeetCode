class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s=list(s)
        moves=0

        while s:
            delta=s.index(s[-1])
            if delta == len(s)-1: #mid character
                moves+= delta//2 
            else:
                moves+=delta
                s.pop(delta)
            s.pop()

        return moves
