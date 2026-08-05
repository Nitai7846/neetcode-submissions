class Solution:
    def climbStairs(self, n: int) -> int:

        def sol(n, memo = {}):

            if n == 0:
                return 1
            
            if n in memo:
                return memo[n]

            if n<0:
                return 0
            
            memo[n] = sol(n-1, memo) + sol(n-2, memo)
            return memo[n]

            
        
        return sol(n, {})

          

            

            
            




          


        