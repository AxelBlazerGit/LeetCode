class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hash = {}
        for word in words:
            temp = ""
            for ch in word:
                temp += ch
                if temp in hash:
                    hash[temp] += 1
                else:
                    hash[temp] = 1
        scores = []
        for word in words:
            temp = ""
            tempscore = 0
            for ch in word:
                temp += ch
                tempscore += hash[temp]
            scores.append(tempscore)
        return scores
