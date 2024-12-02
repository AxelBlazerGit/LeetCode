class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        k=len(searchWord)
        i=1
        for w in sentence.split():
            if w[:k]==searchWord:
                return i
            i+=1
        return -1
