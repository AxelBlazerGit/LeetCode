from collections import Counter
from math import factorial as fact
class Solution:
    def anagramCount(self,word):
        freq=Counter(word)
        numerator=fact(len(word))
        denominator=1
        for count in freq.values():
            denominator*=factorial(count)
        return numerator//denominator
    def countAnagrams(self, s: str) -> int:
        MOD=10**9+7
        words=s.split()
        words=[''.join(sorted(word)) for word in words]
        word_counts=Counter(words)
        ans=1
        for word,count in word_counts.items():
            ans=(ans*pow(self.anagramCount(word),count,MOD)) % MOD
        return ans
