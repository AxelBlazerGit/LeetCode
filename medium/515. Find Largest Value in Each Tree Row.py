# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq=deque([root])
        values=[]
        def bfs():
            while dq:
                n=len(dq)
                lvlmax=-2**31
                for i in range(n):
                    node=dq.popleft()
                    lvlmax=max(lvlmax,node.val)
                    if node.right:
                        dq.append(node.right)
                    if node.left:
                        dq.append(node.left)
                values.append(lvlmax)
        bfs()
        return values
