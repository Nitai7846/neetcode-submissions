# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0 
        

        def dfs(node):

            if not node:
                return (0,0) 
            
            l_rob, left_skip = dfs(node.left)
            r_rob, right_skip = dfs(node.right)

            rob_here = node.val + left_skip + right_skip 
            rob_skip = max(l_rob, left_skip) + max(r_rob, right_skip)

            return (rob_here, rob_skip)
        
        return max(dfs(root))

            

        