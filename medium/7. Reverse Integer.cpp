class Solution {
public:
    int reverse(int x) {
        bool flag = false;
        if (x < 0) flag = true;
        int rev = 0;
        while (abs(x) > 0) {
            int digit = x % 10;
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && digit > 7)) return 0; 
            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && digit < -8)) return 0; 
            rev = rev * 10 + digit;
            x /= 10;
        }
        // if (flag) return -rev;
        return rev;
    }
};
