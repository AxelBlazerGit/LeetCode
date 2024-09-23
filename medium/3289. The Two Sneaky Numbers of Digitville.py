class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky=[]
        hash={}
        for i in nums:
            if i not in hash:
                hash[i]=True
            else:
                sneaky.append(i)
                if len(sneaky)==2:
                    return sneaky
