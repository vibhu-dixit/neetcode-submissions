# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inordertraverse(node):
            if not node:
                return

            inordertraverse(node.left)
            inordertraverse(node.right)
            res.append(node.val)

        inordertraverse(root)
        return res