# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 
        
        self.count = 0
        
        def dfs(root, maxVal):

            if not root:
                return 0
            
            if root.val >= maxVal:
                self.count +=1
            
            maxVal = max(root.val, maxVal)
            dfs(root.left, maxVal) 
            dfs(root.right, maxVal)
        
        dfs(root, root.val)
        return self.count
            
            
                