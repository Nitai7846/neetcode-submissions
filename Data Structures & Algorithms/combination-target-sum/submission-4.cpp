class Solution {
public:

    void dfs(int i, vector<int>& nums, int target, vector<vector<int>>& res, vector<int>& subset, int curr_val){

        if (i>=nums.size()){
            return;
        }
        if (curr_val > target){
            return;
        }
        if (curr_val == target){
            res.push_back(subset);
            return;
        }

        curr_val += nums[i];
        subset.push_back(nums[i]);
        dfs(i, nums, target, res, subset, curr_val);
        curr_val -= nums[i];
        subset.pop_back();
        dfs(i+1, nums, target, res, subset, curr_val);
        

    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {

        vector<vector<int>> res; 
        vector<int> subset; 
        int curr_val = 0; 
        int i = 0; 

        dfs(0, nums, target, res, subset, 0);
        return res;
        
    }
};
