class Solution:
# assume binary tree like generation from root node 0 to left child 0 and right child 0..return index k-1 node of row n
# binary search to find the index and flip if left child of 1 or right child of 0
    def kthGrammar(self, n: int, k: int) -> int:
        bit=l=0
        r=2**(n-1)-1
        while l<=r:
            m=(l+r)//2
            if k>m+1:
                l=m+1
                bit^=1
            else:
                r=m-1
        return bit
