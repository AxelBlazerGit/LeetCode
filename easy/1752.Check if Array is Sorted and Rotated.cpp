class Solution {
public:
    
    bool check(vector<int>& nums) {
        int n=nums.size();
        int ans=(nums[n-1]>nums[0]) ? 1 : 0 ;
        for(int i=0;i<n-1;i++) if(nums[i]>nums[i+1]) ans++;
        return ans<=1;
    }
};
