class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets=[]
        backpack=[]
        #goal is to remove duplicate subsets, that is the number of elements is the one
        #we track for each element, order does not matter, so to keep same number
        #of numbers in each element.....idk the logic for that
        nums.sort()
        def dfs(i):

            if i>=len(nums):
                subsets.append(backpack[:])
                return
            
            backpack.append(nums[i])
            dfs(i+1)

            backpack.pop()
            while i+1 <len(nums) and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return subsets

            
