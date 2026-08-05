# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        ans = []
        queue.append(root)
        if not root:
            return ans

        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(temp)
    
        return ans
        
        


            



        