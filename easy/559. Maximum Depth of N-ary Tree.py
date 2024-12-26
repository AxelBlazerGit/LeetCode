"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        lvl=[0]
        if not root:
            return lvl[0]
        def dfs(node,cur):
            lvl[0]=max(lvl[0],cur)
            for subnode in node.children:
                dfs(subnode,cur+1)
        dfs(root,1)
        return lvl[0]
