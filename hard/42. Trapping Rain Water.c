int trap(int* height, int heightSize) {
    int l=0,r=heightSize-1,ans=0,mxL=0,mxR=0;
    while(l<=r){
        if(height[l]<=height[r]){
            if(height[l]>=mxL) mxL=height[l++];
            else ans+=mxL-height[l++];
        }else{
            if(height[r]>mxR) mxR=height[r--];
            else ans+=mxR-height[r--];
        }
    }
    return ans;
}
