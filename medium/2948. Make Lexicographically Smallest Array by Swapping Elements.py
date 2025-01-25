class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        chunks=[]
        hash={}
        # form chunks which are sorted in form of abs(chunk[-1]-x)<limit for all new x
        # each chunk is sorted reverse
        # maintain hashmap of chunks from original index
        # pop from respective chunk in original mapping and append to lsa
        for ele in reversed(sorted(nums)):
            if not chunks or abs(ele-chunks[-1][-1])>limit:
                chunks.append([])
            chunks[-1].append(ele)
            hash[ele]=len(chunks)-1
        print(chunks)
        print(hash)
        lsa=[]
        for ele in nums:
            chunk=hash[ele]
            lsa.append(chunks[chunk].pop())
        return lsa

# nums =
# [1,7,28,19,10]
# limit =
# 3
# Stdout
# [[28], [19], [10, 7], [1]]
# {28: 0, 19: 1, 10: 2, 7: 2, 1: 3}
# Output
# []
# Expected
# [1,7,28,19,10]
