class Solution:
    MAX = 10**13

    def mincost(self, robot: List[int], robo: int, factories: List[int], repair: int, dp: List[List[int]]) -> int:
        if robo < 0:
            return 0
        if repair < 0:
            return self.MAX
        if dp[robo][repair] != -1:
            return dp[robo][repair]
        
        include = abs(robot[robo] - factories[repair]) + self.mincost(robot, robo - 1, factories, repair - 1, dp)
        exclude = self.mincost(robot, robo, factories, repair - 1, dp)
        
        dp[robo][repair] = min(include, exclude)
        return dp[robo][repair]
    
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        factories = []
        for pos, count in factory:
            factories.extend([pos] * count)
        
        dp = [[-1] * len(factories) for _ in range(len(robot))]
        return self.mincost(robot, len(robot) - 1, factories, len(factories) - 1, dp)
