class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        to_remove = set()
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        to_remove = to_remove.union(set(stack))
        final = []
        for i, ch in enumerate(s):
            if i not in to_remove:
                final.append(ch)
        return "".join(final)
