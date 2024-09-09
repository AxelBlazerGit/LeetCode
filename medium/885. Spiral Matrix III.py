class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        path,step=[],1
        r, c = rStart, cStart
        path.append([r,c])
        ele=rows*cols
        # pseudo : 
        # walk right 1 step
        # walk down 1 step
        # walk left 2 step
        # walk up 2 step
        # walk right 3 step..
        # => if step is x=>right x,down x,left x+1,up x+1,right x+2..
        # step repeat is twice and then increment..
        # append to path arr if -1<i<rows and -1<j<cols till len(path)==row*col
        def add_to_path(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                path.append([r, c])
        while len(path) < ele:
            # Move right
            for _ in range(step):
                c += 1
                add_to_path(r, c)
            # Move down
            for _ in range(step):
                r += 1
                add_to_path(r, c)
            step += 1
            # Move left
            for _ in range(step):
                c -= 1
                add_to_path(r, c)
            # Move up
            for _ in range(step):
                r -= 1
                add_to_path(r, c)
            step += 1
        return path[:ele]
