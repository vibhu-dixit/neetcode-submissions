# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return (0, 0)
            L, R = dfs(root.left), dfs(root.right)
            return (max(L) + max(R), root.val + L[0] + R[0])
        return max(dfs(root))