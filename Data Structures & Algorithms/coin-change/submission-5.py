class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        cache = [-1]*(amount+1)
        

        def dfs(remaining):

            if remaining == 0:
                return  0
            
            if remaining < 0:
                return float('inf')
            
            if cache[remaining] != -1:
                return cache[remaining]
                
            best = float('inf') 
            for i in range(0, n):

                best = min(best, 1+dfs(remaining-coins[i]))
                cache[remaining] = best
            
            return cache[remaining]
        
        res =  dfs(amount)
        return res if res!=float('inf') else -1 
            




        