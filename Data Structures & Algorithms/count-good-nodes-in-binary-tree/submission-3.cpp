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
    int good = 0;

    void dfs(TreeNode* root, int maxVal){
        if (root == nullptr){
            return;  
        }
        if (root->val >= maxVal){
            good++;
        }
        maxVal = max(root->val, maxVal); 
        dfs(root->left, maxVal); 
        dfs(root->right, maxVal);
    }

    int goodNodes(TreeNode* root) {

        if (root == nullptr){
            return 0;
        }

        dfs(root, root->val);
        return good;


        
        
    }
};
