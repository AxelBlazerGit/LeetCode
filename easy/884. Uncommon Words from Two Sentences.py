class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        temp=Counter(s1.split(" ")+s2.split(" "))
        return [word for word,cnt in temp.items() if cnt==1]
