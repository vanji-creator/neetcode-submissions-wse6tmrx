class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #i need a final answer array and a backpack array
        #from my understanding of that tree, i have to simulate that
        #tree behaviour
        #at each level, two choices, lets say levels start from front of
        #array or back of the array, it doesnt really matter
        #if from front then inclue that and go to next choice,
        #again if there any more elements include that and go
        #then when the end is reached, use that backpack in the result<
        #now to backtrack, undo ur previous task that is exclude
        #again after reaching the previous state, make the other choice
        #of excluding it and add that backpack to the result array
        #i think i should go back to the initial state again, am not sure of this
        #part alone, this is confusing me
        answerArray=[]
        backpack=[]
        def dfs(i):
            if i>=len(nums):
                answerArray.append(backpack.copy())
                return
            
            backpack.append(nums[i])
            dfs(i+1)

            backpack.pop()
            dfs(i+1)
        
        dfs(0)
        return answerArray

        