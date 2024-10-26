# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hashL = [0] * (10**5 + 1)
    hashR = [0] * (10**5 + 1)
    high = 0

    def left(self, root, depth):
        if not root:
            return
        Solution.hashL[root.val] = Solution.high
        Solution.high = max(Solution.high, depth)
        self.left(root.left, depth + 1)
        self.left(root.right, depth + 1)

    def right(self, root, depth):
        if not root:
            return
        Solution.hashR[root.val] = Solution.high
        Solution.high = max(Solution.high, depth)
        self.right(root.right, depth + 1)
        self.right(root.left, depth + 1)

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        Solution.high=0
        self.left(root, 0)
        Solution.high = 0
        self.right(root, 0)
        return [max(Solution.hashR[i], Solution.hashL[i]) for i in queries]
