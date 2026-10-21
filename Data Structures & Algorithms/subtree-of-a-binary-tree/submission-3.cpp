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

    bool sameTree(TreeNode* node1, TreeNode* node2) {

        if (node1 == nullptr && node2 == nullptr) {
            return true;
        }

        else if (node1 == nullptr || node2 == nullptr) {
            return false;
        }

        else if (node1->val != node2->val) {
            return false;
        }

        else {
            return sameTree(node1->left, node2->left) &&
                   sameTree(node1->right, node2->right);
        }
    }

    bool dfs(TreeNode* root, TreeNode* subRoot) {

        if (root == nullptr) {
            return false;
        }

        bool ans = sameTree(root, subRoot);

        if (ans == true) {
            return true;
        }

        else {
            return dfs(root->left, subRoot) ||
                   dfs(root->right, subRoot);
        }
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        return dfs(root, subRoot);
    }
};