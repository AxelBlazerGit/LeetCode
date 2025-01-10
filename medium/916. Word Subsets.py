class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        check=defaultdict(int)
        for i in words2:
            temp=Counter(i)
            for i in temp:
                check[i]=max(check[i],temp[i])
        subs=[]
        for i in words1:
            temp=Counter(i)
            flag=True
            for k in check:
                if temp[k]<check[k]:
                    flag=False
                    break
            if flag:
                subs.append(i)
        return subs
