class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        hash={}
        def countt(n=0):
            if n>high:
                return 0
            if n in hash:
                return hash[n]
            hash[n]=1 if n>=low else 0
            hash[n]+=countt(n+zero)+countt(n+one)
            return hash[n]%(10**9+7)
        return countt()%(10**9+7)
