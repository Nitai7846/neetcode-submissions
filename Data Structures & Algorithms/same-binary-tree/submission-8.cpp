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
    bool isSame = true;

    void dfs(TreeNode* root1, TreeNode* root2) {

        if (root1 == nullptr && root2 == nullptr) {
            return;
        }

        if (root1 == nullptr || root2 == nullptr) {
            isSame = false;
            return;
        }

        if (root1->val == root2->val) {
            dfs(root1->left, root2->left);
            dfs(root1->right, root2->right);
        }

        if (root1->val != root2->val) {
            isSame = false;
            return;
        }
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        isSame = true;
        dfs(p, q);
        return isSame;
    }
};