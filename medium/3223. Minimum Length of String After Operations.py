class Solution:
    def minimumLength(self, s: str) -> int:
        s=Counter(s)
        for k in s:
            if s[k]>=3:
                if s[k]%2:
                    s[k]=1
                else:
                    s[k]=2
        return sum(s.values())
# 4=>2
# 5=>3=>1
# 6=>4>2
# if n%2:
#     n=1
# n=2
# aaabbbb
# abb
