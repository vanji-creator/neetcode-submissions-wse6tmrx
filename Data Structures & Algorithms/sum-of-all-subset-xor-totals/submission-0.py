class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xorSum=0
        backpack=[]
        def dfs(i):
            nonlocal xorSum,backpack
            if i>=len(nums):
                #perform xor on the backpack, and update xorSum
                currentXor=0
                for num in backpack:
                    currentXor ^= num
                xorSum+=currentXor
                return
            
            backpack.append(nums[i])
            dfs(i+1)

            backpack.pop()
            dfs(i+1)
        
        dfs(0)
        return xorSum