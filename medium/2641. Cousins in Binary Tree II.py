# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq.append((root.val, root))
        while dq:
            n = len(dq)
            levelSum = 0
            for temp, node in dq:
                levelSum += node.val
                
            for i in range(n):
                temp, node = dq.popleft()
                child = 0
                if node.left: child += node.left.val
                if node.right: child += node.right.val
                if node.left: dq.append((child, node.left))
                if node.right: dq.append((child, node.right))
                node.val = levelSum - temp  
        return root
