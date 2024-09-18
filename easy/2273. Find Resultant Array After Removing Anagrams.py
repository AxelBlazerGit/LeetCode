class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans=[word for word in words]
        for i in range(len(words)-1):
            if sorted(words[i])==sorted(words[i+1]):
                ans[i+1]=None
        return [word for word in ans if word]
