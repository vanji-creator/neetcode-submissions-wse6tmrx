class Solution:
    def totalNQueens(self, n: int) -> int:
        numberOfSolutions=0
        cols=set()
        posDiag=set()
        negDiag=set()

        def checker(r,c):
            if c in cols:
                return False
            elif r+c in posDiag:
                return False
            elif r-c in negDiag:
                return False
            return True
        
        def dfs(r):
            nonlocal numberOfSolutions
            if r==n:
                numberOfSolutions+=1
                return
            for c in range(n):
                if checker(r,c):
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    cols.add(c)
                    dfs(r+1)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    cols.remove(c)
            return False
        
        dfs(0)
        return numberOfSolutions
