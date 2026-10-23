/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */



class Solution {
public:
    bool dfs(TreeNode* root, long long left_val, long long right_val) {
        if (root == nullptr) {
            return true;
        }

        if (root->val <= left_val) {
            return false;
        }
        else if (root->val >= right_val) {
            return false;
        }

        return dfs(root->left, left_val, root->val) &&
               dfs(root->right, root->val, right_val);
    }

    bool isValidBST(TreeNode* root) {
        return dfs(root, LLONG_MIN, LLONG_MAX);
    }
};
