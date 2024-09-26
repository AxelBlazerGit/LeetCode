class MyCalendar:

    def __init__(self):
        self.calendar=list()

    def book(self, start: int, end: int) -> bool:
        for st,ed in self.calendar:
            if start<ed and end>st:
                return False
        self.calendar.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
