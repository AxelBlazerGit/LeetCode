class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False
class Solution:
    def insert(self, word: str, root: TrieNode):
        node = root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isLast = True
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            self.insert(word, root)
        n = len(s)
        arr = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            arr[i] = arr[i + 1] + 1
            node = root
            for j in range(i, n):
                index = ord(s[j]) - ord('a')
                if not node.children[index]:
                    break
                node = node.children[index]
                if node.isLast:
                    arr[i] = min(arr[i], arr[j + 1])
        return arr[0]
