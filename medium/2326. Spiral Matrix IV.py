# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans=[[-1]*n for k in range(m)]
        left, right = 0, n
        top, bottom = 0, m
        if not head:
            return ans
        while head:
            # l=>r:
            for i in range(left,right):
                if head:
                    ans[top][i]=head.val
                    head=head.next
                else:
                    return ans
            top+=1
            # top=>bottom
            for i in range(top,bottom):
                if head:
                    ans[i][right-1]=head.val
                    head=head.next
                else:
                    return ans
            right-=1
            # right=>left:
            for i in range(right-1,left-1,-1):
                if head:
                    ans[bottom-1][i]=head.val
                    head=head.next
                else:
                    return ans
            bottom-=1
            # bottom=>top:
            for i in range(bottom-1,top-1,-1):
                if head:
                    ans[i][left]=head.val
                    head=head.next
                else:
                    return ans
            left+=1
        return ans

