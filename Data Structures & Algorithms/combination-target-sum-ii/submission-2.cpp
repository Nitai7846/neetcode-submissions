
class Solution {
public:

    void dfs(int i, vector<int>& nums, int target,
             vector<vector<int>>& res,
             vector<int>& subset, int curr_val) {

        if (curr_val == target) {
            res.push_back(subset);
            return;
        }

        if (i >= nums.size() || curr_val > target) {
            return;
        }

        // Include nums[i]
        subset.push_back(nums[i]);
        dfs(i + 1, nums, target, res, subset, curr_val + nums[i]);

        // Backtrack
        subset.pop_back();

        // Skip duplicates when excluding
        while (i + 1 < nums.size() && nums[i] == nums[i + 1]) {
            i++;
        }

        // Exclude nums[i]
        dfs(i + 1, nums, target, res, subset, curr_val);
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {

        sort(candidates.begin(), candidates.end());

        vector<vector<int>> res;
        vector<int> subset;

        dfs(0, candidates, target, res, subset, 0);

        return res;
    }
};

