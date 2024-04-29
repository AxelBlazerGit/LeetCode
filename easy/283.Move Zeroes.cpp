class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int curr=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0)swap(nums[curr++],nums[i]);
            // for(int j=0;j<nums.size();j++){
            //     if(nums[j]!=0) swap(nums[curr++],nums[j]);
            // }
        }
    }
};
