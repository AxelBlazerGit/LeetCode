class Solution {
public:
    bool isCharacterPresent(char ch, const string& word) {
        return word.find(ch) != string::npos;
    }
    vector<string> findWords(vector<string>& words) {

        string arr[] = {"qwertyuiopQWERTYUIOP", "ASDFGHJKLasdfghjkl",
                        "ZXCVBNMzxcvbnm"};

        vector<string> ans;
        

        for (auto ele : words) {
            bool flag = true;
            for (int i = 0; i < 3; i++) {

                if (isCharacterPresent(ele[0], arr[i])) {

                    for (int x = 1; x < ele.length(); x++) {

                        if (!isCharacterPresent(ele[x], arr[i])) {
                            flag = isCharacterPresent(ele[x], arr[i]);
                            break;
                        }
                    }
                    if (flag)
                        ans.push_back(ele);

                    continue;
                }
            }
        }
        return ans;
    }
};
