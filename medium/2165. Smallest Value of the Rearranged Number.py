class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<=0:
            return -1*(int("".join(sorted(str(-num))[::-1])))
        num=sorted(str(num))
        if num[0]!="0":
            return(int("".join(num)))
        for i in range(len(num)):
            if num[i]!="0":
                return int(num[i] + "".join(num[:i]) + "".join(num[i+1:]))
