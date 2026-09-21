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

        # BFS approach
        stack = [root]
        while stack:
            node = stack.pop(0)
            #swap
            node.left, node.right = node.right, node.left
            #go down further to check other levels
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

            


