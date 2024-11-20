# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        temp=head
        if not head.next:   return None
        while temp:
            size+=1
            temp=temp.next
        temp=head
        if n==size: return head.next
        for i in range(size-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
