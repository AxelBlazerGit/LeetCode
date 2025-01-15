class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def bits(x):
            return bin(x)[2:].count('1')
        n1,n2=bits(num1),bits(num2)
        temp=num1
        idx=0
        while n2>n1: # to set bits
            if not temp & (1<<idx):
                n2-=1
                temp|= 1<<idx
            idx+=1
        while n1>n2: # unset bits
            if temp & (1<<idx):
                n1-=1
                temp^=1<<idx
            idx+=1
        return temp
