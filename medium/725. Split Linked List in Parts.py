# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# pseudo : convert entire LL to 1D arr..n=len of arr..if n<k then each LL in result will have one value
# with some being none
# if n==k then all sub LL are of size 1
# if n//k>=k then we firstly create a result array that has an int value of how much sized LL it can hold
# firstly we distribute evenly..that is n//k elements for each.. and set aside n%k..that is:
# these many leftmost LL will have one greater size than LL on the right..
# so we increment n%k values in result..
# then we allocate in result the subarrays that need to be returned..these are in 1D array form as of now..
# we then convert each 1D array to LL and return
class Solution:
    def allocate_elements(self, arr, result):
        allocated = []
        index = 0
        for count in result:
            if index < len(arr):
                allocated.append(arr[index:min(index + count, len(arr))])
                index += count
            else:
                allocated.append([])
        return allocated
    def array_to_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        result = [n // k] * k
        remainder = n % k
        for i in range(remainder):
            result[i] += 1
        result = self.allocate_elements(arr, result)
        list_of_linked_lists = [self.array_to_linked_list(sub_arr) for sub_arr in result]
        return list_of_linked_lists
