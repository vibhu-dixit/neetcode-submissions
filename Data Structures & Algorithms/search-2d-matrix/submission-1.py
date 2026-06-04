class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        column=len(matrix[0])
        l,r=0,row-1
        while l<=r:
            mid=(l+r)//2
            if target>matrix[mid][-1]:
                l=mid+1
            elif target<matrix[mid][0]:
                r=mid-1
            else:
                break
        row=(l+r)//2
        l, r = 0, column - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False