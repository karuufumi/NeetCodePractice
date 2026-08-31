# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorderRec(root,res):
            if root is None:
                return
            res.append(root.val)
            preorderRec(root.left,res)
            preorderRec(root.right,res)
        res=[]
        preorderRec(root,res)
        return res


        