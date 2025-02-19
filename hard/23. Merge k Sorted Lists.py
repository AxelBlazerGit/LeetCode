# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for idx,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,idx,node))
        merged=ListNode()
        tail=merged
        while heap:
            val,idx,node=heapq.heappop(heap)
            tail.next=node
            tail=node
            if node.next:
                heapq.heappush(heap,(node.next.val,idx,node.next))
        return merged.next
