# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: 
            return 
        
        #DFS - Recursive
        root.left, root.right = root.right, root.left

        #recursion on left part
        self.invertTree(root.left)
        #recursion on right part
        self.invertTree(root.right)

        return root
            


