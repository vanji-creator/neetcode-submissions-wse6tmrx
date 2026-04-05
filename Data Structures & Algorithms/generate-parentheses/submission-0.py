class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #this will be recursion (backtracking solution)
        #at each level, i will have two choices, either add new set of ()
        #or cover the existing (())
        #in this solution i thought passing backpack as a parameter would
        #be more efficient

        parantheses=[]
        backpack=""

        def dfs(openCount,closeCount,backpack):
            if len(backpack)==n*2:
                parantheses.append(backpack)
                return
            
            if openCount<n:
                dfs(openCount+1,closeCount,backpack+"(")

            if closeCount<openCount:
                dfs(openCount,closeCount+1,backpack+")")
        
        dfs(0,0,backpack)
        return parantheses

