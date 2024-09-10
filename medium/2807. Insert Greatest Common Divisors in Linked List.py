# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current and current.next:
            nxt=current.next
            new=ListNode(self.gcd(current.val, current.next.val))
            current.next=new
            new.next= nxt
            current=nxt
        return head
