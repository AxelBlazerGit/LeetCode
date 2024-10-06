class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # can add sentence substring in start/middle/end
        sentence1=sentence1.split(' ')
        sentence2=sentence2.split(' ')
        if len(sentence1)>len(sentence2):
            sentence1,sentence2=sentence2,sentence1
        n1=len(sentence1)
        pref=suf=0
        while pref<n1 and sentence1[pref]==sentence2[pref]:
            pref+=1
        while suf<n1-pref and sentence1[-(suf+1)]==sentence2[-(suf+1)]:
            suf+=1
        return pref+suf==n1
