# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
# use set to make lookups constant time
# use dummy LL and form it while traversing nums
# connect next pointers only if required
# return dummy
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(next=head)
        current = dummy
        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
