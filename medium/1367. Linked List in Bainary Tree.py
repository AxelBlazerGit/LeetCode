# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self,ll,tn):
        if not ll:
            return True
        if not tn or ll.val!=tn.val:
            return False
        return self.check(ll.next,tn.left) or self.check(ll.next,tn.right)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.check(head,root):
            return True
        if not root:
            return False
        return self.isSubPath(head,root.right) or self.isSubPath(head,root.left)
# isubpath=> from the head keep traversing in one depth of tree.. if list exhausted and matching=> found
# not matching=>go for other childnode
# do this recursively for all childnodes as well
        
