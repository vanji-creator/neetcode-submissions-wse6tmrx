class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #i have to back track,
        #base condition is the number less than sum, if its equal to sum
        #copy the array to result
        #if its larger than sum then discard, use same elements until it exceeds sum
        #then back track and use diff element
        #but i dont have a clear vision of how the diff element will be used 
        #while backtracking like the deciding factor for that
        currentSum=0
        backpack=[]
        res=[]

        def dfs(i,currentSum):

            if currentSum==target:
                res.append(backpack[:])
                return
            
            if i>=len(nums) or currentSum>target:
                return
            
            backpack.append(nums[i])
            dfs(i,currentSum+nums[i])

            backpack.pop()
            dfs(i+1,currentSum)
        
        dfs(0,currentSum)
        return res