class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int n = prices.size(); 


        int left = 0;
        int right = 1; 

        int profit = 0; 

        while (right < n){

            if (prices[left] <= prices[right]){
                profit += prices[right] - prices[left];

            }

            left++;
            right++;


        }

        return profit;

        



        
        

    }
};