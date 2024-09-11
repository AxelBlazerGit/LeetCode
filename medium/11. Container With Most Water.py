class Solution:
# we since we dont need to worry about the heights being like physical containers..
# we can simply traverse to find max area possible with two pointers
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        ans=0
        while r-l:
            ans=max(ans,(r-l)*min(height[r],height[l]))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return ans
