class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        # money=0
        fives=0
        tens=0
        for bill in bills:
            if bill==5:
                fives+=1
            elif bill==10:
                fives-=1
                tens+=1
            else:
                fives-=1 if tens>0 else 3
                tens-=1 if tens else 0
            if fives<0:
                return False
        return True if fives>=0 else False
