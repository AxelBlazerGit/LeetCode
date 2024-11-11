primes = []
class Solution:
    def sieve(self, n):
        global primes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(2, n + 1) if is_prime[i]]

    def binS(self, t):
        global primes
        left, right = 0, len(primes) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if primes[mid] <= t:
                result = primes[mid]
                left = mid + 1
            else:
                right = mid - 1
        return result

    def primeSubOperation(self, nums: List[int]) -> bool:
        self.sieve(max(nums))
        cur = 0
        for ele in nums:
            target = ele - cur - 1
            sub = self.binS(target) if target > 0 else -1
            if sub == -1:
                if ele <= cur:
                    return False
                cur = ele
            else:
                next = ele - sub
                if next <= cur:
                    return False
                cur = next
        return True
