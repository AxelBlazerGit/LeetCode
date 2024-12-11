class Solution:
    def sieve(self,limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False

        for num in range(2, int(limit**0.5) + 1):
            if sieve[num]:
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False
        primes = {i for i, is_prime in enumerate(sieve) if is_prime}
        return primes
    def findPrimePairs(self, n: int) -> List[List[int]]:
        pairs=[]
        if n<4:
            return pairs
        primes=self.sieve(n)
        for i in range(2,n//2+1):
            if i in primes and n-i in primes:
                pairs.append([i,n-i])
        return pairs
