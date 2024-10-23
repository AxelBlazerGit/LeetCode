# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # bfs
        queue = deque([(root, None, 0)])  # parent,depth
        X,Y=None,None
        while queue:
            node, parent, depth = queue.popleft()
            
            if node.val == x:
                X = (parent, depth)
            elif node.val == y:
                Y = (parent, depth)
            
            if X and Y:
                break
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
        
        if X and Y:
            xp, xd = X
            yp, yd = Y
            return xd == yd and xp != yp
        
        return False
