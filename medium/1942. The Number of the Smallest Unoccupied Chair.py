class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Sort friends by their arrival time
        events = sorted(range(len(times)), key=lambda i: times[i][0])
        # List of available chairs
        available = list(range(len(times)))  # Initially, all chairs are available
        occupied = []  # Min-heap to track occupied chairs (when they will be free)
        # Process each friend in the order of their arrival
        for friend in events:
            arrival, leave = times[friend]
            # Free any chairs from friends who have already left
            while occupied and occupied[0][0] <= arrival:
                heapq.heappush(available, heapq.heappop(occupied)[1])
            # Assign the smallest available chair to the current friend
            assigned = heapq.heappop(available)
            # If this is the target friend, return the chair number
            if friend == targetFriend:
                return assigned
            # Mark the chair as occupied until the friend leaves
            heapq.heappush(occupied, (leave, assigned))
