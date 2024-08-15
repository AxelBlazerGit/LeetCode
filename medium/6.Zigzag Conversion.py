class Solution:
    def convert(self, text: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(text):
            return text
        result = [''] * numRows  # List to store characters for each row
        row = 0
        direction = 1  # 1 means down, -1 means up
        
        for char in text:
            result[row] += char  # Add current character to the current row
            
            # Update row and direction based on current position
            if row == 0:
                direction = 1  # Change direction to down when reaching top row
            elif row == numRows - 1:
                direction = -1  # Change direction to up when reaching bottom row
            
            row += direction  # Move to the next row
        
        return ''.join(result)  # Concatenate all rows into a single string
