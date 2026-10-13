class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_profit = 0 

        left = 0
        right = 1
        

        while right < n:

            if prices[left] <= prices[right]:

                max_profit += prices[right] - prices[left]
                right+=1
                left+=1
                
            
            elif prices[left] > prices[right]:
                right+=1 
                left+=1 
                
            
        
        return max_profit 




        


        
        
        