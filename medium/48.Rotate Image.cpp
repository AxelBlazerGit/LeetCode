#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // pseudo : transpose then reverse columns : 
        //be careful with transposing twice* since traversing entire matrix will cause nullification of transpose
        //hence j=i+1 
        // Transpose
        for(int i = 0; i < matrix.size(); i++) {
            for(int j = i + 1; j < matrix.size(); j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        // Reverse columns
        int left = 0, right = matrix.size() - 1;
        while(left < right) {
            for(int row = 0; row < matrix.size(); row++) {
                swap(matrix[row][left], matrix[row][right]);
            }
            left++;
            right--;
        }
    }
};
