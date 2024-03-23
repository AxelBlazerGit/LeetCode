class Solution {
public:
    bool hasRepeatedFrequency(const std::vector<int>& vec) {
        map<int, int> frequencyMap;
        for (int element : vec) {
            frequencyMap[element]++;
        }

        unordered_set<int> frequencySet;

        for (const auto& pair : frequencyMap) {
            if (frequencySet.find(pair.second) != frequencySet.end()) {
                return true;
            }
            frequencySet.insert(pair.second);
        }

        return false; 
    }
    bool uniqueOccurrences(vector<int>& arr) {
        return !hasRepeatedFrequency(arr);
    }
};
