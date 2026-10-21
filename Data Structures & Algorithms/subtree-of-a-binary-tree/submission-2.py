# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def sameTree(root1, root2):

            if root1 == None and root2 == None:
                return True 
            
            elif root1 and not root2:
                return False 
            
            elif root2 and not root1:
                return False
            
            elif root1.val != root2.val:
                return False
            
            else:
                return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
        
        def dfs(root):

            if root is None:
                return False 
            
            ans = sameTree(root, subRoot)
            if ans == True:
                return True 
            else:
                return dfs(root.left) or dfs(root.right)

        return dfs(root)     
            

                
                
            


            


        