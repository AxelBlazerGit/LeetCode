class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        def flip(x):
            return 0 if x else 1 
        msb=cur=0
        for bit in derived:
            if bit:
                cur=flip(cur)
        return msb==cur
