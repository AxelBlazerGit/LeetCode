class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
            prevbest=values[0] # values[0] + 0
            bestPair=0
            for i in range(1,len(values)):
                this=values[i]-i
                curPair=prevbest+this
                bestPair=max(curPair,bestPair)
                prevbest=max(prevbest,values[i]+i)

            return bestPair
