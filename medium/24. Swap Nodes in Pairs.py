# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
            
        temp = ListNode()
        temp.next=head
        i, j = temp, head

        while j and j.next:
            nxt = j.next.next
            swap = j.next
            
            swap.next = j
            j.next = nxt
            i.next = swap
            
            i = j
            j = nxt
        return temp.next
