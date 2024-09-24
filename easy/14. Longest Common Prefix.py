class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def put(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    def findLcp(self, total_words: int) -> str:
        node = self.root
        prefix = []
        while len(node.children) == 1:
            char, next = list(node.children.items())[0]
            if next.count == total_words: 
                prefix.append(char)
                node = next
            else:
                break
        return ''.join(prefix)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs=set(strs)
        trie = Trie()
        for word in strs:
            trie.put(word)
        return trie.findLcp(len(strs))
