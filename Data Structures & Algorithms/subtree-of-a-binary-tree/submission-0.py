# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, Root: Optional[TreeNode], SubRoot: Optional[TreeNode]) -> bool:
        if not SubRoot: return True
        if not Root: return False
        if self.sametree(Root,SubRoot): return True
        return self.isSubtree(Root.left,SubRoot) or self.isSubtree(Root.right,SubRoot)

    def sametree(self,Root,SubRoot):
        if not Root and not SubRoot:
            return True
        if Root and SubRoot and Root.val==SubRoot.val:
            return self.sametree(Root.left,SubRoot.left) and self.sametree(Root.right,SubRoot.right)
        return False
            