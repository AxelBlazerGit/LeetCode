class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<pair<int, int>> counts;
        int n = nums.size();

        for (auto ele : nums) {
            auto it = find_if(counts.begin(), counts.end(),
                              [ele](const pair<int, int>& element) {
                                  return element.first == ele;
                              });

            if (it != counts.end()) {
                it->second++;
            } else {
                counts.push_back({ele, 1});
            }
        }

        vector<int> ans;
        for (const auto& kv : counts) {
            float fraction = static_cast<float>(n) / kv.second;
            if (fraction < 3) {
                ans.push_back(kv.first);
            }
        }

        return ans;
    }
};
