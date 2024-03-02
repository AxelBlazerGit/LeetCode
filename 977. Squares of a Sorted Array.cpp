class Solution {
public:
    void bubble(vector<int>& arr) {
        int n = arr.size();
        for (int i = n - 1; i > 0; i--) {
            int check = 0;
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    check = 1;
                }
            }
            if (check == 0) break;
        }
        for (auto ele : arr) cout << ele << " ";
        cout << endl;
    }
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> arr(nums.size(), 0);
        int i = 0;
        for (auto it : nums) arr[i++] += it * it;

        // Using bubble sort to sort the squared values
        bubble(arr);

        return arr;
    }
};
