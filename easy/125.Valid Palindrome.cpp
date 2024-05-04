class Solution {
public:
    string modify(string str){
        string temp="";
        for(char i:str){
            if((i>64 and i<91) or (i>96 and i<123) or (i>='0' and i<='9')){
                if(i>64 and i<91) temp+=i-'A'+'a';
                if(i>96 and i<123) temp+=i;
                if(i>='0' and i<='9') temp+=i;
            }
        }return temp;
    }
    bool isPalindrome(string str) {
        str=modify(str);
        int s=0,e=str.size()-1;
        while(s<e) if(str[s++]!=str[e--]) return false;
        return true;
    }
};
