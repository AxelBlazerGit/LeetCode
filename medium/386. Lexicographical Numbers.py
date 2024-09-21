class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans=[]
        def recurse(i):
            if i>n:
                return
            ans.append(i)
            for j in range(10):
                temp=i*10+j
                recurse(temp)
        for i in range(9):
            recurse(i+1)
        return ans
