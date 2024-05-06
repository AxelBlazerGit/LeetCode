class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        //pseudo:
        // since matrix is sorted for rows only
        // we begin from last column first row
        // if found return true
        // if target exceeds this then move to next row since all previous values cant contain target
        // if target is lesser than pointer then move a column left
        int r=matrix.size(),c=matrix[0].size();
        int i=0,j=c-1;
        while(i<r and j>=0){
            if (matrix[i][j]==target) return true;
            if(matrix[i][j]<target) i++;
            else j--;
        }
        return false;
    }
};
