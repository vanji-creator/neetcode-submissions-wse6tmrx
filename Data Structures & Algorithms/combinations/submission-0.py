class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results=[]
        backpack=[]
        
        def dfs(i):
            if len(backpack)==k:
                results.append(backpack[:])
                return

            if i > n:
                return
            
            backpack.append(i)
            dfs(i+1)

            backpack.pop()
            dfs(i+1)
        
        dfs(1)
        return results