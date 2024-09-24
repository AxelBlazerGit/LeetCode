class Solution:
  # using string comparison
  def isPrefixAndSuffix(self, word1: str, word2: str) -> bool:
      m = len(word1)
      return word2[:m] == word1 and word2[-m:] == word1
  def countPrefixSuffixPairs(self, words: List[str]) -> int:
      count = 0
      n = len(words)
      for i in range(n):
          for j in range(i + 1, n):
              word1 = words[i]
              word2 = words[j]
              if self.isPrefixAndSuffix(word1, word2):
                  count += 1
      return count

# TRIE DOES NOT WORK YET
  
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end = False
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#     def put(self, word: str):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.end = True
#     def is_prefix(self, word: str) -> bool:
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True
    # using trie
    # def countPrefixSuffixPairs(self, words: List[str]) -> int:
    #     prefixTrie = Trie()
    #     suffixTrie = Trie()
    #     for word in words:
    #         prefixTrie.put(word)
    #         suffixTrie.put(word[::-1])
    #     count = 0
    #     n = len(words)
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             word1 = words[i]
    #             word2 = words[j]
    #             if prefixTrie.is_prefix(word1) and suffixTrie.is_prefix(word2[::-1]):
    #                 count += 1
    #     return count



    
