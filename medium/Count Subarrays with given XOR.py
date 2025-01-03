import collections
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        hash=collections.defaultdict(int)
        xor=subs=0
        for i in arr:
            xor^=i
            if xor==k:
                subs+=1
            subs+=hash[xor^k]
            hash[xor]+=1
        return subs
