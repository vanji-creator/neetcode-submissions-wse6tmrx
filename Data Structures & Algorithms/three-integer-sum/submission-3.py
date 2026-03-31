class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        check=set()
        ans=set()
        nums.sort()
        for i in range(1,len(nums)):    
            check.add(nums[i-1])
            for j in range(i+1,len(nums)):
                if -(nums[i]+nums[j]) in check:
                    ans.add((nums[i],nums[j],-(nums[i]+nums[j])))
        
        return [list(x) for x in ans]
