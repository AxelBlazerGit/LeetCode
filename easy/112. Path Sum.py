# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root,cur):
            if not root:
                return False
            # cur*=10
            cur+=root.val
            # if cur==targetSum:  return True
            if not root.right and not root.left:    return cur==targetSum
            return traverse(root.left,cur) or traverse(root.right,cur)
        return traverse(root,0)
