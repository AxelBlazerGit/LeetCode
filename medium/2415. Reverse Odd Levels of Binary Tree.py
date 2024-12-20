# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])
        lvl = 0

        while dq:
            if lvl & 1:
                l, r = 0, len(dq) - 1
                while l < r:
                    dq[l].val, dq[r].val = dq[r].val, dq[l].val
                    l += 1
                    r -= 1
            lvl += 1

            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    dq.append(node.right)

        return root
