# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.isSameTree = True 

        def dfs(root1, root2):

            if not root1 and not root2:
                return 
            
            if root1 and not root2:
                self.isSameTree = False 
                return 
            
            if root2 and not root1:
                self.isSameTree = False 
                return
            
            if root1.val == root2.val:
                dfs(root1.left, root2.left)
                dfs(root1.right, root2.right)
            
            if root1.val != root2.val:
                self.isSameTree = False 
            
        dfs(p, q)
        return self.isSameTree

            
            



        