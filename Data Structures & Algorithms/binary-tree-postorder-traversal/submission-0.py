# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderRec(self,root,res):
        if root is None:
            return
        self.postorderRec(root.left,res)
        self.postorderRec(root.right,res)
        res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorderRec(root,res)
        return res