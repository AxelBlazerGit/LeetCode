# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        o=head
        e=head.next
        eHead=e
        while e and e.next:
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        o.next=eHead
        # e.next=None
        return head
