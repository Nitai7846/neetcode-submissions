class Solution:

    def func(self, i, buy, n, prices, dp):

        if i >= n:
            return 0 

        if dp[i][buy] != -1:
            return dp[i][buy]
        
        profit = 0 

        if buy == 0:
            profit = max(0+self.func(i+1, 0, n, prices,dp) , -prices[i] +self.func(i+1,1,n,prices, dp))

        if buy == 1:
            profit = max(0+self.func(i+1, 1, n, prices,dp), prices[i]+self.func(i+2, 0, n, prices,dp))
        
        dp[i][buy] = profit
        

        return dp[i][buy]



    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n ==0 :
            return 0 
        
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        ans = self.func(0,0,n,prices,dp)


        return ans 

        
            



        