class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #i have nxn spaces available, each time a place a queen, i have
        # one row, one column, one diagonal lesser than before
        #i have to try different combinations and store the ones that are possible
        #i have to use backtracking and recursion because it will help me
        #explore different combinations in a problem


        results=[]
        cols=set()
        posDiag=set()
        negDiag=set()
        backpack=[["."]*n for _ in range(n)]

        def checker(r,c):
            if c in cols:
                return False
            elif r+c in posDiag:
                return False
            elif r-c in negDiag:
                return False
            return True
        
        def dfs(r):
            if r==n:
                results.append(["".join(row) for row in backpack])
                return
            
            for c in range(n):
                if checker(r,c):
                    backpack[r][c]="Q"
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    cols.add(c)
                    dfs(r+1)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    cols.remove(c)
                    backpack[r][c]="."
            return False
        
        dfs(0)
        return results
        
            
