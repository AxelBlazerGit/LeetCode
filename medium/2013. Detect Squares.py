class DetectSquares:

    def __init__(self):
        self.hash=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.hash[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        squares=0
        dx,dy=point
        for x,y in self.hash:
            if not(abs(dx-x)!=abs(dy-y) or x==dx or y==dy):
                if (dx,y) in self.hash and (x,dy) in self.hash:
                    squares+=self.hash[(x,y)]*self.hash[(dx,y)]*self.hash[(x,dy)]
        return squares

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
