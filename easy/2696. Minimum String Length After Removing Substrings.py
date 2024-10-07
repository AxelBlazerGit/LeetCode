class Solution:
    def minLength(self, s: str) -> int:
        # two pointer approach
        s = list(s)
        j = 0

        for i in range(len(s)):
            s[j] = s[i]
            j += 1
            if j >= 2 and (s[j-2] == 'A' and s[j-1] == 'B' or s[j-2] == 'C' and s[j-1] == 'D'):
                j -= 2

        return j


# class Solution:
#     def minLength(self, s: str) -> int:
          # stack approach 
#         stk=list()
#         for ch in s:
#             stk.append(ch)
#             if stk[-2:]==['A','B'] or stk[-2:]==['C','D']:
#                 stk.pop()
#                 stk.pop()
#         return len(stk)
