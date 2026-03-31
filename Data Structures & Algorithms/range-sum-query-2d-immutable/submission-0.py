class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefix=[[0] * len(self.matrix[0]) for _ in range(len(self.matrix))]        
        i=0
        while i < len(self.matrix):
            j=0
            while j <len(self.matrix[0]):
                self.prefix[i][j]=self.matrix[i][j]+(self.prefix[i][j-1] if j>0 else 0)
                j+=1
            i+=1


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i=row1
        j=col1
        res=0
        while i <=row2:
            res+=self.prefix[i][col2] - (self.prefix[i][col1-1] if col1>0 else 0) 
            i+=1
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)