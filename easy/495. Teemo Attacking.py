class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # timeSeries=sorted(list(set(timeSeries)))
        if len(timeSeries)==1:
            return duration
        
        poison=duration

        for i in range(1,len(timeSeries)):
            reset=1 if (duration>timeSeries[i]-timeSeries[i-1]) else 0
            poison+=timeSeries[i]-timeSeries[i-1] if reset else duration
        return poison
