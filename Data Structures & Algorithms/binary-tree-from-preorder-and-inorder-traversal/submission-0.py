# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inMap = {val: idx for idx, val in enumerate(inorder)}

        # Recursive helper function to build the tree
        def helper(preStart, preEnd, inStart, inEnd):
            # Base case: If the start indices
            # exceed the end indices, return null
            if preStart > preEnd or inStart > inEnd:
                return None

            # Create a new TreeNode with value
            # at the current preorder index
            root_val = preorder[preStart]
            root = TreeNode(root_val)

            # Find the index of the current root
            # value in the inorder traversal
            inRoot = inMap[root_val]

            # Calculate the number of
            # elements in the left subtree
            numsLeft = inRoot - inStart

            # Recursively build the left subtree
            root.left = helper(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)

            # Recursively build the right subtree
            root.right = helper(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)

            # Return the current root node
            return root

        # Call the helper function to build the tree
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        