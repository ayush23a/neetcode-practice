"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if root == None:
            return []

        ans = []
        st1 = [root]
        st2 = []

        while st1:
            node = st1.pop()
            st2.append(node)

            if node.children:
                for child in node.children:
                    st1.append(child)
            
        while st2:
            node = st2.pop()
            ans.append(node.val)

        return ans
        