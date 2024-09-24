class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def put(self, num: int):
        node = self.root
        for digit in str(num):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.end = True

    def lcp(self, num: int) -> int:
        node = self.root
        length = 0
        for digit in str(num):
            if digit in node.children:
                node = node.children[digit]
                length += 1
            else:
                break
        return length
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.put(num)
        max_length = 0
        for num in arr2:
            max_length = max(max_length, trie.lcp(num))
        return max_length
