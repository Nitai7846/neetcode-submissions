class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(amount):

            if amount == 0:
                return 0 

            if amount in memo:
                return memo[amount]

            res = 1e9 
            for i in range(0, len(coins)):

                if amount - coins[i] >= 0:
                    res = min(res, 1+dfs(amount-coins[i]))

            memo[amount] = res
            
            return res 

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

        
                
                
                

                
            

            
        