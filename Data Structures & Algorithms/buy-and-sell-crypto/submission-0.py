class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0 
        n = len(prices)
        i , j = 0, 1
        while j < n:
            if prices[j] > prices[i]:
                ans = max(ans, prices[j] - prices[i])
                j+=1
            else:
                i = j
                j = i+1 
        
        return ans 
            


        