class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        c,pdiag,ndiag=set(),set(),set()
        solve=[]
        board=[['.']*n for _ in range(n)]
        def bt(r):
            if r==n:
                solve.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in c or (r+col) in pdiag or (r-col) in ndiag:
                    continue
                c.add(col)
                pdiag.add(r+col)
                ndiag.add(r-col)
                board[r][col]='Q'
                bt(r+1)
                c.remove(col)
                pdiag.remove(r+col)
                ndiag.remove(r-col)
                board[r][col]='.'
        bt(0)
        return solve
