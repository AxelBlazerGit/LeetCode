class Solution:
    # def swap(self,arr,x,y)
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,m,h=0,0,len(arr)-1
        while(m<=h):
            if(arr[m]==0):
                arr[l],arr[m]=arr[m],arr[l]
                m+=1
                l+=1
            elif(arr[m]==2):
                arr[m],arr[h]=arr[h],arr[m]
                h-=1
            else:
                m+=1
