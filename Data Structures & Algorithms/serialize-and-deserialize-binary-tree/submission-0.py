# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []

        def pre_order(node: TreeNode | None):
            ret.append(str(node.val) if node else "N")
            if node:
                pre_order(node.left)
                pre_order(node.right)

        pre_order(root)
        return ":".join(ret)

    def construct(self, elements: list[int | None], i: int) -> tuple[Optional[TreeNode], int]:
        if i >= len(elements) or (el := elements[i]) is None:
            return None, i
        el_tree = TreeNode(el)
        el_tree.left, i = self.construct(elements, i + 1)
        el_tree.right, i = self.construct(elements, i + 1)
        return el_tree, i

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        return self.construct([int(e) if e != "N" else None for e in data.split(":")], 0)[0]