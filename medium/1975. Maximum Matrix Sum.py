class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ### observation : a negative when flipped with a positive, ###
        # can be moved across matrix and only one num is -ve
        # therefore => even count of -ve can be made positive
        # for odd count of -ve =>
        # matrix will have at least one negative element remaining
        # after flipping as many negatives as possible into positives
        # to maximize sum, minimize impact of remaining negative number, 
        # so we flip smallest positive number or least negative number 
        # if no positives remain
        s=x=0
        minPositive=float('inf')
        maxNegative=-minPositive
        for i in matrix:
            for j in i:
                if j<0:
                    x+=1
                    s-=j
                    maxNegative=max(maxNegative,j)
                else:
                    s+=j
                    minPositive=min(minPositive,j)
        if x&1:
            return s-2*min(-maxNegative,minPositive)
        return s
