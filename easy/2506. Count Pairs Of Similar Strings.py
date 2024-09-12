class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words=[set(i) for i in words]
        similar=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i]==words[j]:# or len(words[i]^words[j])==1:
                    similar+=1
        return similar
