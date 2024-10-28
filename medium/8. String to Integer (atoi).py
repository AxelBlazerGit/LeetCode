class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        neg = False
        i = 0
        if s[0] == '-':
            neg = True
            i = 1
        elif s[0] == '+':
            i = 1
        integer = 0
        while i < len(s) and s[i].isdigit():
            integer = integer * 10 + int(s[i])
            i += 1
        if neg:
            integer = -integer
        
        MIN = -2**31
        MAX = 2**31 - 1
        if integer < MIN: integer = MIN
        elif integer > MAX:   integer = MAX
        
        return integer
