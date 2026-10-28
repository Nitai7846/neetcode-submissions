class Solution {
public:

    void dfs(vector<int>& nums, vector<vector<int>>& ans,
             vector<int>& res, vector<bool>& picked) {

        int n = nums.size();

        if (res.size() == n) {
            ans.push_back(res);
            return;
        }

        for (int i = 0; i < n; i++) {

            if (picked[i] == false) {
                res.push_back(nums[i]);
                picked[i] = true;

                dfs(nums, ans, res, picked);

                res.pop_back();
                picked[i] = false;
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {

        int n = nums.size();

        vector<vector<int>> ans;
        vector<int> res;
        vector<bool> picked(n, false);

        dfs(nums, ans, res, picked);

        return ans;
    }
};