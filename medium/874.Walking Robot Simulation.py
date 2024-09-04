# return max euclidean distance
# if robot runs into obstacle it will stay there at {one less} x/y coordinate and do further tasks
# -1 is turn right -2 is left
# start from 0,0 facing north

# solution: 
# keep two vars x,y for currPosn,ans to store x2+y2
# always check if we are encountering obstacle and new xy then is either one less than obstacle or as input suggests
# 4conditions for 4directions
# maintain direction by

# current_direction = 0  # Start facing North

# if turn == -1:  # Turn right
#         current_direction = (current_direction + 1) % 4
#     elif turn == -2:  # Turn left
#         current_direction = (current_direction - 1) % 4
# class Solution:
#     def interrupted(self,x1, y1, x2, y2, obstacles):
#         # Vertical line (same x-coordinates)
#         if x1 == x2:
#             for obstacle in obstacles:
#                 ox, oy = obstacle
#                 # Check if the obstacle is on the same vertical line and between the y-values
#                 if ox == x1 and min(y1, y2) <= oy <= max(y1, y2):
#                     return True
#         # Horizontal line (same y-coordinates)
#         elif y1 == y2:
#             for obstacle in obstacles:
#                 ox, oy = obstacle
#                 # Check if the obstacle is on the same horizontal line and between the x-values
#                 if oy == y1 and min(x1, x2) <= ox <= max(x1, x2):
#                     return True
#         # No obstacle found in between
#         return False
#     def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
#         directions = ['N', 'E', 'S', 'W']
#         # obstacles=set(obstacles)
#         curr=0
#         x,y=0,0
#         ans=0
#         dir=(-1*curr)%4
#         for command in commands:
#             if command>0: # walk
#                 if not curr: # northBound => change in y
#                     y2=y+command
#                     if self.interrupted(x,y,x,y2,obstacles):
#                         y+=command-1
#                     else:
#                         y+=command
#                 elif curr==2: # southBound => change in y
#                     y2=y-command
#                     if self.interrupted(x,y,x,y2,obstacles):
#                         y-=command-1
#                     else:
#                         y-=command
#                 elif curr==1: # eastBound => change in x
#                     x2=x+command
#                     if self.interrupted(x,y,x2,y,obstacles):
#                         x+=command-1
#                     else:
#                         x+=command
#                 else: # westBound => change in x
#                     x2=x-command
#                     if self.interrupted(x,y,x2,y,obstacles):
#                         x-=command-1
#                     else:
#                         x-=command
#                 ans=max(ans,x*x+y*y)
#             else: # turn
#                 if command == -1:  # Turn right
#                     curr = (curr + 1) % 4
#                 elif command == -2:  # Turn left
#                     curr = (curr - 1) % 4
#         return ans



class Solution:
    def interrupted(self, x1, y1, x2, y2, obstacles):
        # verticalLine
        if x1 == x2:
            for ox, oy in obstacles:
                if ox == x1 and min(y1, y2) <= oy <= max(y1, y2):
                    return True
        # horizontalLine
        elif y1 == y2:
            for ox, oy in obstacles:
                if oy == y1 and min(x1, x2) <= ox <= max(x1, x2):
                    return True
        # path clear
        return False
    
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # legend = ['N', 'E', 'S', 'W']
        curr = 0  # north initially
        if [0, 0] in obstacles:
            obstacles.remove([0, 0])
        x, y = 0, 0
        euclideanDist = 0
        
        for command in commands:
            if command > 0:  # walk
                if curr==0: # northBound => change in y
                    for _ in range(command):
                        if self.interrupted(x, y, x, y + 1, obstacles):
                            break
                        y += 1
                elif curr==2: # southBound => change in y
                    for _ in range(command):
                        if self.interrupted(x, y, x, y - 1, obstacles):
                            break
                        y -= 1
                elif curr==1: # eastbound => change in x
                    for _ in range(command):
                        if self.interrupted(x, y, x + 1, y, obstacles):
                            break
                        x += 1
                elif curr==3: # westBound => change in x
                    for _ in range(command):
                        if self.interrupted(x, y, x - 1, y, obstacles):
                            break
                        x -= 1
                
                euclideanDist = max(euclideanDist, x*x + y*y)
            else:  # turn
                if command == -1:  # right
                    curr = (curr + 1) % 4
                elif command == -2:  # left
                    curr = (curr - 1) % 4
        
        return euclideanDist


