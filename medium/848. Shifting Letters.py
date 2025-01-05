class Solution:
    def ascii(self, s: str) -> list[int]:
        return [ord(char) - ord('a') for char in s]
    def strAscii(self, lst: list[int]) -> str:
        return ''.join(chr(num + ord('a')) for num in lst)
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        s=self.ascii(s)
        for i in range(len(s)):
            s[i]+=shifts[i]
            s[i]%=26
        return self.strAscii(s)
