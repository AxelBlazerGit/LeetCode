class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        loons=1
        points.sort()
        r=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=r:
                r=min(points[i][1],r)
            else:
                loons+=1
                r=points[i][1]
        return loons
            # 1     6
            #  2           8
