class Solution {
public:
    void rev(vector<int>&nums,int s,int e){
        while(s<e){
            swap(nums[s++],nums[e--]);
        }
    }
    void rotate(vector<int>& nums, int k) {
        k%=nums.size();
        rev(nums,0,nums.size()-1);
        rev(nums,0,k-1);
        rev(nums,k,nums.size()-1);
        
    }
    //7 6 5 4 3 2 1
    //5 6 7
    //5 6 7/1 2 3 4
};
