# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node):
            if not node:
                return None

            left = traverse(node.left)
            right = traverse(node.right)

            new_node = TreeNode(node.val, right, left)
            return new_node
        
        return traverse(root)