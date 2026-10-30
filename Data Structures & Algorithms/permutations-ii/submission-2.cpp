class Solution {
public:
    void dfs(vector<int>& nums,
             unordered_map<int, int>& count,
             vector<int>& perm,
             vector<vector<int>>& res) {

        if (perm.size() == nums.size()) {
            res.push_back(perm);
            return;
        }

        for (auto& [n, freq] : count) {
            if (freq > 0) {
                perm.push_back(n);
                freq--;

                dfs(nums, count, perm, res);

                freq++;
                perm.pop_back();
            }
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> perm;
        unordered_map<int, int> count;

        for (int n : nums) {
            count[n]++;
        }

        dfs(nums, count, perm, res);
        return res;
    }
};