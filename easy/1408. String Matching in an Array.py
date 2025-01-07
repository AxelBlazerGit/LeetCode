class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subs=set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    subs.add(words[i])
        return list(subs)
