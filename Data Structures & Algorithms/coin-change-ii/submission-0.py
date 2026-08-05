class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        def dfs(i, remaining, n):

            if i>=n:
                return 0 
            
            if remaining<0:
                return 0 
            
            if dp[i][remaining]!=-1:
                return dp[i][remaining]

            if remaining == 0:
                return 1 

            res = 0 

            res = dfs(i+1, remaining, n) + dfs(i, remaining-coins[i], n)

            dp[i][remaining] = res 

            return dp[i][remaining]

        return dfs(0, amount, n)
            




        