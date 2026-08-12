# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(node1, node2):

            if node1 == None and node2 == None:
                return True
            elif node1 == None and node2 != None or node1 != None and node2 == None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)
        

        def dfs(root):

            if root is None:
                return False
            
            ans = sameTree(root, subRoot)
            if ans == True:
                return True 
            
            else:
                return dfs(root.left) or dfs(root.right)

        return dfs(root)
        
        
            
            
                
        

        
        