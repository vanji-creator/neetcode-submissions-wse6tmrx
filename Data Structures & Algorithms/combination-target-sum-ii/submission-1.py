class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res=set()
        res=[]
        backpack=[]
        currentSum=0
        candidates.sort()

        def dfs(i,currentSum):
            if currentSum==target:
                # res.add(tuple(backpack[:]))
                res.append(backpack[:])
                return 
            
            if i>=len(candidates) or currentSum>target:
                return

            backpack.append(candidates[i])
            dfs(i+1,currentSum+candidates[i])

            backpack.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,currentSum)
        
        dfs(0,currentSum)
        # return [list(backpackElement) for backpackElement in res]
        return res