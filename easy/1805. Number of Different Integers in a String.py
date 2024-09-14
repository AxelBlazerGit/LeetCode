class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        temp=set()
        tempst=''
        for i in word:
            if '0' <= i <= '9':
                tempst += i
            else:
                if tempst != '':
                    temp.add((int(tempst)))
                tempst = ''
        if tempst != '':
            temp.add(int(tempst))
        return len(temp)
