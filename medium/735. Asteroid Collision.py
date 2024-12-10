class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        aftermath=list()
        for i in asteroids:
            while aftermath and aftermath[-1]>0 and i<0:
                check=aftermath[-1]+i
                if not check:
                    i=0
                    aftermath.pop()
                elif check>0:
                    i=0
                else:
                    aftermath.pop()
                    # aftermath.append(i)
            if i:
                aftermath.append(i)
            
        return aftermath
