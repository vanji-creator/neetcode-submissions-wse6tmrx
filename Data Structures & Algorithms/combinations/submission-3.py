class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations=[]
        backpack=[]


        def dfs(i):
            if len(backpack)==k:
                combinations.append(backpack[:])
                return
            if i>n:
                return
            
            if len(backpack) + (n-i+1)<k:
                return
            backpack.append(i)
            # print(backpack,"first choice")
            dfs(i+1)

            backpack.pop()
            # print(backpack,"second choice")
            dfs(i+1)

        dfs(1)
        return combinations
