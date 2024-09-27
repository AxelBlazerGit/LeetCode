class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find the time when each car arrives in sorted manner of positions
        # if a car can overtake it becomes a fleet=> no use of multiple cars as a fleet
        # => return finally the independent cars that would be representing their fleets
        # => emulate checking for overtake via stack
        time = sorted([(posn, vel) for posn, vel in zip(position, speed)], reverse=True)
        fleets = []
        for ds, dv in time:
            fleets.append((target - ds) / dv)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)
