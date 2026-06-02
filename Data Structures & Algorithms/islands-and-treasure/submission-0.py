from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #have to start with the gates in the queue, so bfs spreads out 
        #from the gates at the same time
        #so that the closest gate reaches first
        rows=len(grid)
        cols=len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue=deque()
        def bfs():
            level=1
            while queue:
                for i in range(len(queue)):
                    r,c=queue.popleft()
                    for dr,dc in directions:
                        nr=r+dr
                        nc=c+dc

                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]>level:
                            grid[nr][nc]=level
                            queue.append((nr,nc))
                level+=1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    queue.append((i,j))
        
        bfs()
        return 