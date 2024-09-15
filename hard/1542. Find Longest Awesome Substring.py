class Solution:
    # 10 digits 2 states=>count has parity even or odd for a subarray
    # total states=>2^10=1024
    # bitmask all digits
    # palindrome=>each digit is 2x[parity0] or only one digit is 2x+1[parity1]
    # parity0 can be checked by creation of visited states
    # parity1 needs to be checked for each digit separately=>tempBitMasks
    def longestAwesome(self, s: str) -> int:
        if len(set(s))==len(s):
            return 1
        ans=mask=0
        visited={0:-1}
        for i in range(len(s)):
            mask^=1<<int(s[i])
            if mask not in visited:
                visited[mask]=i
            ans=max(ans,i-visited[mask])
            for x in range(10):
                tempMask=mask^(1<<x)
                if tempMask in visited:
                    ans=max(ans,i-visited[tempMask])
        return ans
