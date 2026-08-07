class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(curr):
            if not curr:
                return 0

            left = height(curr.left)    
            if left == -1:              # if unbalanced
                return -1               # don't check right subtree

            right = height(curr.right)
            if right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
        return height(root) > -1