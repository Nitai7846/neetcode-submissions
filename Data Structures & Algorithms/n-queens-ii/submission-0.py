class Solution:
    def totalNQueens(self, n: int) -> int:

        res = []
        board = [['.']*n for _ in range(n)]
        cols = set()
        diags1 = set()
        diags2 = set()

        def dfs(r):

            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):

                if c not in cols and (r-c) not in diags1 and (r+c) not in diags2:

                    board[r][c] = 'Q'
                    cols.add(c)
                    diags1.add(r-c)
                    diags2.add(r+c)

                    dfs(r+1)

                    board[r][c] = '.'
                    cols.remove(c)
                    diags1.remove(r-c)
                    diags2.remove(r+c)
            
        dfs(0)
        return len(res)
                    

                    
