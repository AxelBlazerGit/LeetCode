class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        cur = 0
        for i in range(len(str1)):
            if(str1[i] == str2[cur] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[cur]):
                cur += 1
            if cur == len(str2):
                return True
        return False
