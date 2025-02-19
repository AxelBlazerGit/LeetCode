# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return "#"

        serial = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                serial.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serial.append("#")

        return ",".join(serial)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "#":
            return None

        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            if i < len(arr) and arr[i] != "#":
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1

            if i < len(arr) and arr[i] != "#":
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
