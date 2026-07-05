"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,row,col):
            is_same=True
            for i in range(n):
                for j in range(n):
                    if grid[row][col]!=grid[row+i][col+j]:
                        is_same=False
                        break
            if True==is_same:
                return Node (grid[row][col],True)
            n=n//2
            topleft=dfs(n,row,col)
            topright=dfs(n,row,col+n)
            bottomright=dfs(n,row+n,col+n)
            bottomleft=dfs(n,row+n,col)
            return Node(0,False, topleft,topright,bottomleft,bottomright)
        return dfs(len(grid),0,0)