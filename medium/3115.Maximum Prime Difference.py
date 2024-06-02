class Solution:
    def isPrime(self,n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    def primes(self,arr):
        temp=[]
        for idx,i in enumerate(arr):
            if self.isPrime(i):
                temp.append(idx)
        return temp
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        idx=self.primes(nums)
        if not idx:
            return 0
        return abs(max(idx)-min(idx))
