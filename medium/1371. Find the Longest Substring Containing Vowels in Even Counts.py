class Solution:
    # 5vowels with 2parity each=>2^5combination;
    # bitmasking=>if s[i] is a vowel update the respective vowels parity
    # since even parity substring is answer=>two same masks can have the substring in between them
    # use hash for previous masks
    def findTheLongestSubstring(self, s: str) -> int:
        ans=0
        visited={0:-1}
        hash={'a':0,'e':1,'i':2,'o':3,'u':4}
        mask=0
        # if s[0] in hash:
        #     mask^=1<<hash[s[0]]
        for i in range(len(s)):
            if s[i] in hash:
                mask^=1<<hash[s[i]]
            if mask not in visited:
                visited[mask]=i
            ans=max(ans,i-visited[mask])
        return ans
