class MyCalendarTwo:
    def __init__(self):
        self.events=list()
        self.intersections=list()
        
    def book(self, start: int, end: int) -> bool:
        for st,ed in self.intersections:
            if end>st and ed>start:
                return False
        for st,ed in self.events:
             if end>st and ed>start:
                self.intersections.append([max(st,start),min(ed,end)])
        self.events.append([start,end])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
