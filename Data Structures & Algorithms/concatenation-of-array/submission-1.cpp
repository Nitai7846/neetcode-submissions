class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {

        int n = nums.size();
        int new_n = 2 * n; 

        vector<int> ans(2*n, 0);

        for (int i =0; i<n; i++){
            ans[i] = nums[i];
            ans[i+n] = nums[i];
            
        }

        return ans ;
        
    }
};