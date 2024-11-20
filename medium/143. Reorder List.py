# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:   return
        f=s=head
        while f and f.next:
            s=s.next
            f=f.next.next
        stack = []
        cur=s.next
        while cur:
            stack.append(cur)
            cur=cur.next
        s.next=None
        cur=head
        while cur and stack:
            node=stack.pop()
            node.next=cur.next
            cur.next=node
            cur=node.next
        if stack:
            node=stack.pop()
            node.next=cur.next
            cur.next=node
# 1 2 3 4 5 6 7
# 1 '7' 2 '6' 3 '5' 4

# 1 2 3 4 5 6 7 8
# 1 '8' 2 '7' 3 '6' 4 '5'   
# fast slow
# f=1 3 5 7
# s=1 2 3 4
# f=1 3 5 7 =
# s=1 2 3 4
# odd=>we exhaust stack before end
# even=>we need to append at end
# s ke baad wala stack mein push karo
# while stack:
#     append b/w head and head.next
#     head=head.next.next
