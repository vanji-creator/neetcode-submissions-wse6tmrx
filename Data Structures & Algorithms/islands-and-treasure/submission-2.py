from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque()
        visited=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    visited.add((i,j))
                    queue.append((i,j))
        dist=1
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if (nr,nc) not in visited and 0<=nr<rows and 0<=nc<cols and grid[nr][nc]>dist:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        grid[nr][nc]=dist
            if len(queue)>0:
                dist+=1
        
        
                    