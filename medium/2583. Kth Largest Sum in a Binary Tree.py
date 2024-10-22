# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:    return -1
        row=list()
        q=deque([root])
        heap=[]
        while q:
            n=len(q)
            temp=0
            for i in range(n):
                node=q.popleft()
                temp+=node.val
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            heapq.heappush(heap,temp)
            if len(heap)>k:
                heapq.heappop(heap)
        return -1 if len(heap)<k else heapq.heappop(heap)
