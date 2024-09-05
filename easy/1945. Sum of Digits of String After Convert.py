class Solution:
    def sum(self,num):
        s=0
        while num:
            s+=num%10
            num//=10
        return s
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        hash = {chr(i): i - 96 for i in range(97, 123)}
        for ch in s:
            num += str(hash[ch])
        num=int(num)
        for i in range(k):
            num=self.sum(num)
        return num
