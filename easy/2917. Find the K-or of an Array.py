class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        kor=0
        for i in range(32):
            count=0
            for n in nums:
                if (n>>i)&1:
                    count+=1
                if count==k:
                    kor |= (1 << i)
                    break
        return kor
