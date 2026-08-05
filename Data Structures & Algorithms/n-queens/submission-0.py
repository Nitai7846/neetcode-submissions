class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [["."]*n for _ in range(n)]
        cols = set()
        diags = set()
        antidiags = set()
    

        def dfs(r):

            if r == n:

                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):

                if c not in cols and (r-c) not in diags and (r+c) not in antidiags:


                    board[r][c] = 'Q'
                    cols.add(c)

                    diags.add(r-c)
                    antidiags.add(r+c)

                    dfs(r+1)

                    board[r][c] = "."
                    cols.remove(c)
                    diags.remove(r-c)
                    antidiags.remove(r+c)
            
        
        dfs(0)
        return res 






        