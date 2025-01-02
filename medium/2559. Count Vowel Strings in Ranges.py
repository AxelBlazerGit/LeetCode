class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix=[0]*(len(words)+1)
        vowels=set("aeiou")
        ans=[]

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i+1]=prefix[i]+1
            else:
                prefix[i+1]=prefix[i]

        for i in range(len(queries)):
            l,r=queries[i]
            ans.append(prefix[r+1]-prefix[l])
        return ans
