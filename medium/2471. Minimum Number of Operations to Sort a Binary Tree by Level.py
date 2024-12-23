# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swap(arr, moves):
            sort = sorted(arr)
            hash = {val: idx for idx, val in enumerate(arr)}

            for i in range(len(arr)):
                while arr[i] != sort[i]:
                    idx = hash[sort[i]]
                    hash[arr[i]] = idx
                    hash[sort[i]] = i
                    arr[i], arr[idx] = arr[idx], arr[i]
                    moves += 1
            return moves

        dq=deque()
        dq.append(root)
        swaps=0
        while dq:
            n=len(dq)
            arr=[]
            for i in range(n):
                node=dq.popleft()
                arr.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            swaps=swap(arr,swaps)
        return swaps
