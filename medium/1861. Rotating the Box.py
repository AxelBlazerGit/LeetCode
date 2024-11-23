class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r, c = len(box), len(box[0])
        rotate = [['.'] * r for _ in range(c)]

        for row in range(r):
            ph=c-1 # placeholder
            for cur in range(c-1,-1,-1):
                if box[row][cur] == '#':
                    rotate[ph][r - row - 1] = '#'
                    ph-=1
                elif box[row][cur] == '*':
                    rotate[cur][r - row - 1] = '*'
                    ph=cur-1
        return rotate
