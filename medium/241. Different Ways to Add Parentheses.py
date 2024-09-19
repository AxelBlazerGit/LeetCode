class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        recurse=self.diffWaysToCompute
        ans=[]
        for i in range(len(expression)):
            if expression[i] in "+-*":
                temp1=recurse(expression[:i])
                temp2=recurse(expression[i+1:])
                for a in temp1:
                    for b in temp2:
                        # ans.append(int(eval(f"{a} {expression[i] {b}}")))
                        ans.append(eval(f"{a} {expression[i]} {b}"))
        if not ans:
            ans.append(int(expression))
        return ans
