from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque()
        currentDistance=1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    # grid[i][j]=float('INF') #for safety
                    queue.append((i,j))
        
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]>currentDistance:
                        grid[nr][nc]=currentDistance
                        queue.append((nr,nc))
            currentDistance+=1
        
        

        
        # return grid