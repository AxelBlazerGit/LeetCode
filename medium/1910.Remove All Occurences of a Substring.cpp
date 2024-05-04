#include <string>

class Solution {
public:
    std::string removeOccurrences(std::string s, std::string part) {
        if (part.length() > s.length()) {
            return s;
        }
        
        size_t index;
        while ((index = s.find(part)) != std::string::npos) {
            s.erase(index, part.length());
        }
        return s;
    }
};
