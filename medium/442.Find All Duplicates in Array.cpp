class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        unordered_set<int> found;
        
        for (int num : nums) {
            if (found.count(num)) {
                ans.push_back(num);
            } else {
                found.insert(num);
            }
        }
        
        return ans;
    }
};
