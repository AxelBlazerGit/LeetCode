class Solution {
public:
    int bitwiseComplement(int n) {
        if(n==0) return 1;
        int copy=n,mask=0;
        while(copy!=0){
            mask=(mask<<1)|1;
            copy=copy>>1;
        }
        return ~n&mask;
    }
};
