class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0  # height, diameter

            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)

            height = 1 + max(lh, rh)
            through = lh + rh
            dia = max(ld, rd, through)
            return height, dia

        return dfs(root)[1]