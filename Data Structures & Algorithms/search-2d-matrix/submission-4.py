class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        l,r=0,rows-1

        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]>target:
                r=mid-1
            elif matrix[mid][-1]<target:
                l=mid+1
            else: 
                break
        row=(l+r)//2
        l,r=0,cols-1
        while l<=r:
            mid=(l+r)//2
            if target>matrix[row][mid]:
                l= mid+1
            elif target<matrix[row][mid]:
                r=mid-1
            else: 
                return True
        return False