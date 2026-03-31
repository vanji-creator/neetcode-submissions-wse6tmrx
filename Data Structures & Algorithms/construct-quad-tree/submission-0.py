class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform(r,c,length):
            first_value=grid[r][c]
            for i in range(r,r+length):
                for j in range(c,c+length):
                    if grid[i][j]!=first_value:
                        return False
            return True
        
        def build(r,c,length):
            if isUniform(r,c,length):
                return Node(grid[r][c]==1,True,None,None,None,None)
            
            half=length//2
            topLeft=build(r,c,half)
            topRight=build(r,c+half,half)
            bottomLeft=build(r+half,c,half)
            bottomRight=build(r+half,c+half,half)

            return Node(True,False,topLeft,topRight,bottomLeft,bottomRight)
        
        return build(0,0,len(grid))