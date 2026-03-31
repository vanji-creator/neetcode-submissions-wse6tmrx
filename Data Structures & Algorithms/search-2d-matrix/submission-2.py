class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=-1
        left,right=0,len(matrix)-1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid][0]<=target:
                row=mid
                left=mid+1
            else:
                right=mid-1


        if row==-1:
            return False
        
        left,right=0,len(matrix[0])-1
        while left<=right:
            mid=(left+right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False