class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permutations=[]

        def dfs(start):
            if start>=len(nums):
                permutations.append(nums[:])
            used=set()
            for i in range(start,len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[start],nums[i]=nums[i],nums[start]
                dfs(start+1)
                nums[start],nums[i]=nums[i],nums[start]
        
        dfs(0)
        return permutations

#i have to avoid duplicates, here duplicates mean same order