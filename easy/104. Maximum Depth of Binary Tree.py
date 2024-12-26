# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=[0]
        if not root:
            return depth[0]
        def dfs(node,cur):
            depth[0]=max(depth[0],cur)
            if node.right:
                dfs(node.right,cur+1)
            if node.left:
                dfs(node.left,cur+1)
        dfs(root,0)
        return depth[0]+1
