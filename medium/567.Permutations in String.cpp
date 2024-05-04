class Solution {
public:
    // vector<string> permute(string s, int l, int r) {
    //     vector<string> result;
    //     if (l == r) {
    //         result.push_back(s);
    //     } else {
    //         for (int i = l; i <= r; ++i) {
    //             swap(s[l], s[i]);
    //             auto permutations = permute(s, l + 1, r);
    //             result.insert(result.end(), permutations.begin(),
    //             permutations.end()); swap(s[l], s[i]);
    //         }
    //     }
    //     return result;
    // }
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) {
            return false;
        }
        int freq[26];
        for (char c : s1)
            freq[c - 'a']++; // hash

        int freq2[26];
        // first sliding window
        for (int i = 0; i < s1.size(); ++i) {
            ++freq2[s2[i] - 'a'];
        }
        if (equal(begin(freq), end(freq), begin(freq2))) {
            return true;
        }

        // rest sliding windows
        for (int i = s1.size(); i < s2.size(); ++i) {
            ++freq2[s2[i] - 'a'];
            --freq2[s2[i - s1.size()] - 'a'];
            if (equal(begin(freq), end(freq), begin(freq2))) {
                return true;
            }
        }

        // permutation dne
        return false;
    }
};
