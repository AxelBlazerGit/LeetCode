class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        # print(intervals)
        erased=-1
        prev=intervals[0][1]
        for cur in intervals:
            if cur[0]<prev:
                erased+=1
            else:
                prev=cur[1]
        return erased
