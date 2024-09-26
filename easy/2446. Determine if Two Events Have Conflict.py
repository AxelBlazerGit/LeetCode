class Solution:
    def minutes(self,time_str):
        hours, minutes = map(int, time_str.split(':')) 
        return hours * 60 + minutes

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1=[self.minutes(i) for i in event1]
        event2=[self.minutes(i) for i in event2]
        if event2[0]>event1[1] or event1[0]>event2[1]:
            return False
        return True
