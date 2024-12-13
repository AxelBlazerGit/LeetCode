class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        freq=sorted(freq.items(), key=lambda x: (x[1], -x[0]))
        new=list()
        for k,f in freq:
            new.extend([k]*f)
        return new
