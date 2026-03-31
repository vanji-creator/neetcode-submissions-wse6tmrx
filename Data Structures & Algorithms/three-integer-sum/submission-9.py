class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        d=set()
        for i in range(1,len(nums)):
            d.add(nums[i-1])  
            for j in range(i+1,len(nums)):
                if -(nums[i]+nums[j]) in d:
                    ans.add(tuple(sorted((nums[i],nums[j],-(nums[i]+nums[j])))))


        return [list(x) for x in ans]