class Solution:
    def bits(self,x):
        return bin(x).count("1")
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr=[[self.bits(i),i] for i in arr]
        arr.sort()
        return [ele for bit,ele in arr ]
