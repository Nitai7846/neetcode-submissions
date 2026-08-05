# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

 

        def dfs(node, min_val, max_val):

            if not node:
                return True 

            if node.val>min_val and node.val<max_val:

                return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

            else:
                return False
        
        min_val = float('-inf')
        max_val = float('inf')

        return dfs(root, min_val, max_val)

            



        

            

            
            
            
            

        