class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        stake=s.count(letter)
        return stake*100//len(s)
