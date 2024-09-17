class Solution:
    # O(N,1)
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev=-1
        ans=0
        n =len(seats)
        for i in range(n):
            if seats[i]:
                if prev==-1:
                    ans=i
                else:
                    ans=max(ans,(i-prev)//2)
                prev = i
        return max(ans,n-1-prev)
            
# class Solution:
    # O(N,N)
    # def maxDistToClosest(self, seats: List[int]) -> int:
    #     start,end=0,0
    #     for i in seats:
    #         if i:
    #             break
    #         start+=1
    #     for  i in seats[::-1]:
    #         if i:
    #             break
    #         end+=1
    #     filled=[]
    #     for i in range(len(seats)):
    #         if seats[i]:
    #             filled.append(i)
    #     ans=max(start,end)
    #     if len(filled)>=2:
    #         for i in range(len(filled[:-1])):
    #             ans=max(ans,(filled[i+1]-filled[i])//2)
    #     return ans
            
