class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        l,r=0,len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]>target:
                r=m-1
            else:
                row=m
                l=m+1

        l,r=0,len(matrix[m])-1
        while l<=r:
            m=(l+r)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]>target:
                r=m-1
            else:
                l=m+1
        return False