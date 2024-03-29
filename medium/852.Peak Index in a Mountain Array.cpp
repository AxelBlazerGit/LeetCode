class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        if(arr.size()==3) return 1;
        int peak,s=0,e=arr.size()-1;
        int mid=s+(e-s)/2;
        while(s<e){
            if(arr[mid]<arr[mid+1]) s=mid+1;
            else e=mid;
            mid=s+(e-s)/2;
        }
        return s;
    }
};
