# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        lb = float('-inf')
        ub = float('inf')

        
        def dfs(root,lb, ub):

            if root is None:
                return True 
            
            if lb<root.val<ub:
                return dfs(root.left, lb, root.val) and dfs(root.right, root.val, ub)
            else:
                return False
            
      
            
        
        return dfs(root, lb, ub)


            
            
            
        