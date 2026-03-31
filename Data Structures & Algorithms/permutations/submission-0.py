class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results=[]
        backpack=[]
        visited=set()

        def dfs():

            if len(backpack)==len(nums):
                results.append(backpack[:])
                return
            
            for number in nums:

                if number in visited:
                    continue
                
                visited.add(number)
                backpack.append(number)
                dfs()

                visited.remove(number)
                backpack.pop()
                
            return

        dfs()
        return results