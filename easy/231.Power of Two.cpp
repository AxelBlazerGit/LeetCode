class Solution {
public:
bool isInteger(double number) {
    return number == floor(number);
}
    bool isPowerOfTwo(int n) {
        if(n==0) return false;
        double logValue = log2(n);
    
        if (isInteger(logValue))    return true;
        else return false;
    }
};
