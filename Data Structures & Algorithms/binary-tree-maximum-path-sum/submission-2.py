# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0 

        curr_max = [root.val]
        
        def dfs(root):

            if not root:
                return 0 
            
            root.left = max(dfs(root.left), 0)
            root.right = max(dfs(root.right), 0)
            curr_max[0] = max(curr_max[0], root.val + root.left + root.right)
            return root.val + max(root.left, root.right)
        
        dfs(root)
        return curr_max[0]


        