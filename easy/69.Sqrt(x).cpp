class Solution {
public:
    int mySqrt(int x) {
        if(x==0 or x==1) return x;
        int s=0,e=x-1,ans=-1;
        long long mid;
        while(s<=e){
            mid=s+(e-s)/2;
            if(mid*mid==x) return mid;
            else if(mid*mid>x) e=mid-1;
            else {s=mid+1;ans=mid;}
        }
        return ans;
    }
};
