class Solution:
    def ascii(self, s: str) -> list[int]:
        return [ord(char) - ord('a') for char in s]
    def strAscii(self, lst: list[int]) -> str:
        return ''.join(chr(num + ord('a')) for num in lst)

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # use a range update approach with a shift array, applying +1 at start index
        # and -1 at end+1 index for each shift, calculate prefix sums over shift 
        # array to determine net shift for each character

        s=self.ascii(s)
        shift=[0]*len(s)
        shift.append(0)

        for i,j,dir in shifts:
            shift[j+1]+=1 if dir else -1
            shift[i]-=1 if dir else -1
        
        curShift=0
        for i in range(len(shift)-1,-1,-1):
              curShift+=shift[i]
              s[i-1] = (26+s[i-1]+curShift)%26

        return self.strAscii(s)
