class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def minutes(time):
            hr,mins=map(int,time.split(":"))
            return hr*60+mins
        if len(timePoints)!=len(set(timePoints)):
            return 0
        timePoints=sorted(timePoints)
        ans=720
        for i in range(1,len(timePoints)):
            ans=min(ans,minutes(timePoints[i])-minutes(timePoints[i-1]))
        ans=min(ans,minutes(timePoints[0])+1440-minutes(timePoints[-1]))
        return ans
        
