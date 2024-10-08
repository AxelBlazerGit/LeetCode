class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        - If n is odd, return False (valid parentheses string must have even length).
        - If first locked character is ')' or last locked character is '(', return False.
        - If there are no '1's in locked string, return True (all positions are adjustable).
        
        First pass: Left-to-right to validate opening parentheses:
        - Initialize checked = 0.
        - Loop over string s from 0 to n-1:
            - If current character is unlocked or '(', increment checked.
            - If locked and ')', decrement checked.
            - If checked becomes negative, return false
        
        Second pass: Right-to-left to validate closing parentheses:
            - If current character is unlocked or ')', increment checked.
            - If locked and '(', decrement checked.
            - If checked becomes negative, return false
        """

        n=len(s)
        if n%2 :
            return False
        if (locked[0]=='1' and s[0] == ')') or (locked[n-1]=='1' and s[n-1] == '('):
            return False
        if '1' not in locked:
            return True
        checked=0
        for i in range(n):
            if locked[i]=='0' or s[i]=='(':
                checked+=1
            else:
                checked-=1
                if checked<0:
                    return False
        checked-=checked
        for i in range(n-1,-1,-1):
            if locked[i]=='0' or s[i]==')':
                checked+=1
            else:
                checked-=1
                if checked<0:
                    return False
        return True
